#!/usr/bin/env python3
"""Build publish-ready HTML for the Fei-Fei Li AI agency deep guide."""

from __future__ import annotations

import html
import re
from pathlib import Path

import markdown


ROOT = Path(__file__).resolve().parent
SOURCE_MD = ROOT / "Fei-Fei_Li_AI_Agency_Future_of_Work_深度導讀.md"
NORMALIZED_MD = ROOT / "article.normalized.md"
OUT_HTML = ROOT / "index.html"


FIGURES = {
    "一、AI 使用者與旁觀者的差距正在擴大": {
        "src": "images/agency-gap.png",
        "mobile": "images/agency-gap-mobile.png",
        "alt": "AI 使用者與旁觀者的差距：旁觀者停在焦慮與觀望，高能動性使用者用 AI 自建工具並重組流程",
        "caption": "AI 的差距不是工具清單，而是誰能把工具接回資料、流程與責任鏈。",
    },
    "二、最危險的不是樂觀或悲觀，而是把 AI 講成二選一": {
        "src": "images/nuanced-middle.png",
        "mobile": "images/nuanced-middle-mobile.png",
        "alt": "AI 兩極敘事與細緻中間路線：烏托邦、末日論與負責任的工具治理問題",
        "caption": "李飛飛提醒，真正需要的是能同時看見能力、限制、增能與風險的細緻中間路線。",
    },
    "三、「智慧成本歸零」是錯誤問題，因為人類智慧不是單一商品": {
        "src": "images/human-intelligence-map.png",
        "mobile": "images/human-intelligence-map-mobile.png",
        "alt": "人類智慧能力地圖：語言、感知、空間、身體、情感與創造力",
        "caption": "語言模型很強，但人類智慧還包含感知、空間、身體、情感與創造力。",
    },
    "六、十年後的公司：職能邊界會變模糊，產品經理是第一個縮影": {
        "src": "images/pm-workflow.png",
        "mobile": "images/pm-workflow-mobile.png",
        "alt": "產品經理工作流前後對照：從數月跨部門循環到 AI 增幅快速原型與驗證",
        "caption": "AI 讓產品經理更早完成初版與驗證，專家則轉向更複雜、更高價值的深化工作。",
    },
    "七、兩種工作者：頂尖專家與高能動性通才": {
        "src": "images/barbell-workers.png",
        "mobile": "images/barbell-workers-mobile.png",
        "alt": "未來人才雙峰結構：頂尖專家與高能動性通才，中等單一技能承壓",
        "caption": "雙峰效應的重點不是職稱，而是頂尖判斷與高能動性都變得更稀缺。",
    },
    "九、空間智慧：大型語言模型之外，AI 還缺一塊古老能力": {
        "src": "images/spatial-agency.png",
        "mobile": "images/spatial-agency-mobile.png",
        "alt": "空間智慧四要素與 agency 培養路徑：理解、推理、生成、互動，以及安全感到獨立判斷",
        "caption": "AI 的完整圖像不能只停在語言；人的完整準備也不能只停在工具操作。",
    },
}


SUMMARY_FIGURE = {
    "src": "images/summary.png",
    "mobile": "images/summary-mobile.png",
    "alt": "一圖看懂 AI 時代的分水嶺：能動性、兩極敘事、使用差距、人類智慧、任務拆解、兩種工作者與空間智慧",
    "caption": "全文總覽：AI 時代真正的分水嶺，是能否把工具轉成能動性與責任。",
}


def slugify(text: str, index: int) -> str:
    mapping = {
        "摘要": "summary",
        "一": "agency-gap",
        "二": "nuanced-middle",
        "三": "human-intelligence",
        "四": "task-breakdown",
        "五": "education",
        "六": "pm-workflow",
        "七": "barbell-workers",
        "八": "thinking-tools",
        "九": "spatial-intelligence",
        "十": "agency-training",
        "十一": "ai-onramp",
        "有洞見": "final-insight",
    }
    for key, value in mapping.items():
        if text.startswith(key):
            return value
    return f"section-{index}"


def split_markdown(md_text: str) -> tuple[str, str]:
    marker = "\n---\n\n## 附錄：逐字稿整理版"
    if marker not in md_text:
        return md_text, ""
    main, appendix = md_text.split(marker, 1)
    return main.strip(), "## 附錄：逐字稿整理版" + appendix


def prepare_sections(md_text: str) -> tuple[str, str, list[tuple[str, str]]]:
    title_match = re.search(r"^#\s+(.+)$", md_text, re.M)
    title = title_match.group(1).strip() if title_match else "Deep Guide"
    sections: list[tuple[str, str]] = []
    counter = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal counter
        counter += 1
        heading = match.group(1).strip()
        section_id = slugify(heading, counter)
        sections.append((section_id, heading))
        return f"## {heading} {{#{section_id}}}"

    prepared = re.sub(r"^##\s+(.+)$", repl, md_text, flags=re.M)
    return title, prepared, sections


def figure_html(figure: dict[str, str], class_name: str = "section-figure") -> str:
    loading_attrs = (
        'loading="eager" decoding="sync" fetchpriority="high"'
        if class_name == "summary-figure"
        else 'loading="lazy"'
    )
    return f"""
<figure class="{class_name}">
  <picture>
    <source media="(max-width: 640px)" srcset="{html.escape(figure["mobile"])}">
    <img src="{html.escape(figure["src"])}" alt="{html.escape(figure["alt"])}" {loading_attrs}>
  </picture>
  <figcaption>{html.escape(figure["caption"])}</figcaption>
</figure>
"""


def inject_figures(body: str) -> str:
    for heading, figure in FIGURES.items():
        section_id = slugify(heading, 0)
        pattern = f'<h2 id="{section_id}">{html.escape(heading)}</h2>'
        body = body.replace(pattern, pattern + figure_html(figure), 1)
    return body


def render_appendix(appendix_md: str) -> str:
    if not appendix_md:
        return ""
    appendix_html = markdown.markdown(appendix_md, extensions=["tables", "fenced_code", "attr_list"])
    appendix_html = re.sub(r"\A<h2[^>]*>.*?</h2>\s*", "", appendix_html, count=1, flags=re.S)
    return f"""
<section class="appendix" id="transcript">
  <details>
    <summary>附錄：逐字稿整理版</summary>
    <div class="appendix-body">
      {appendix_html}
    </div>
  </details>
</section>
"""


def short_nav_label(label: str) -> str:
    label = re.sub(r"^摘要：", "摘要｜", label)
    label = re.sub(r"^[一二三四五六七八九十、]+、", "", label)
    replacements = {
        "AI 使用者與旁觀者的差距正在擴大": "使用差距",
        "最危險的不是樂觀或悲觀，而是把 AI 講成二選一": "細緻中間",
        "「智慧成本歸零」是錯誤問題，因為人類智慧不是單一商品": "智慧地圖",
        "工作不是一個整體被取代，而是一組任務被重新拆解": "任務拆解",
        "教育的問題不再是要不要禁 AI，而是要重設學習目標": "教育重設",
        "十年後的公司：職能邊界會變模糊，產品經理是第一個縮影": "公司未來",
        "兩種工作者：頂尖專家與高能動性通才": "兩種工作者",
        "真正改變工作的工具，不只是回答問題，而是陪你思考": "陪你思考",
        "空間智慧：大型語言模型之外，AI 還缺一塊古老能力": "空間智慧",
        "agency 如何培養：不是技巧清單，而是從尋求讚美轉向追問問題": "培養 agency",
        "給 AI 初學者的入口：找一個年輕人，讓他帶你看一次未來": "初學入口",
        "有洞見的總結：未來十年的分水嶺，是誰能把工具轉化成責任": "總結",
    }
    return replacements.get(label, label[:14])


def render_page(title: str, body: str, appendix: str, sections: list[tuple[str, str]]) -> str:
    nav = "".join(
        f'<a href="#{section_id}">{html.escape(short_nav_label(label))}</a>'
        for section_id, label in sections
        if section_id != "summary"
    )
    return f"""<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <meta name="description" content="李飛飛與 David Rogier 談 AI、agency、未來工作、教育與空間智慧的深度導讀。">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:type" content="article">
  <meta property="og:image" content="images/summary.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="images/summary.png">
  <style>
    :root {{
      color-scheme: light;
      --bg: #f3f0e9;
      --paper: #fffdf8;
      --ink: #252321;
      --muted: #68635d;
      --line: #ded6c8;
      --teal: #2f766f;
      --coral: #b9564e;
      --gold: #b28a3a;
      --soft-teal: #e6f1ee;
      --soft-coral: #f7e7e3;
      --shadow: 0 18px 48px rgba(58, 50, 38, .11);
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      color: var(--ink);
      background:
        linear-gradient(180deg, rgba(255,253,248,.98) 0, rgba(243,240,233,.94) 460px),
        var(--bg);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
      line-height: 1.68;
      letter-spacing: 0;
    }}
    .shell {{ max-width: 1120px; margin: 0 auto; padding: 30px 22px 72px; }}
    .summary-figure {{
      margin: 24px auto 22px;
      padding: 0 10px;
      max-width: 690px;
    }}
    .summary-figure img {{
      display: block;
      width: 100%;
      max-width: 640px;
      margin: 0 auto;
      border-radius: 12px;
      aspect-ratio: 16 / 9;
      object-fit: contain;
      background: var(--paper);
      border: 1px solid var(--line);
      box-shadow: var(--shadow);
      cursor: zoom-in;
    }}
    .summary-figure figcaption, .section-figure figcaption {{
      margin: 10px auto 0;
      max-width: 760px;
      color: var(--muted);
      font-size: .92rem;
      line-height: 1.55;
      text-align: center;
    }}
    header {{
      max-width: 980px;
      margin: 0 auto 26px;
      padding: 12px 0 28px;
      text-align: center;
    }}
    .eyebrow {{
      margin: 0 0 14px;
      color: var(--teal);
      font-weight: 800;
      font-size: .92rem;
    }}
    h1 {{
      margin: 0;
      font-size: clamp(2.15rem, 4.55vw, 3.28rem);
      line-height: 1.11;
      text-wrap: pretty;
    }}
    .dek {{
      max-width: 900px;
      margin: 18px auto 0;
      color: var(--muted);
      font-size: 1.04rem;
    }}
    .meta {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 8px;
      margin: 20px 0 0;
      padding: 0;
      list-style: none;
    }}
    .meta li {{
      padding: 6px 10px;
      border: 1px solid var(--line);
      border-radius: 999px;
      background: rgba(255, 253, 248, .72);
      color: var(--muted);
      font-size: .88rem;
    }}
    .nav {{
      position: sticky;
      top: 0;
      z-index: 20;
      margin: 0 -22px;
      padding: 10px 22px;
      background: rgba(243, 240, 233, .94);
      border-top: 1px solid var(--line);
      border-bottom: 1px solid var(--line);
      backdrop-filter: blur(12px);
      overflow-x: auto;
      white-space: nowrap;
    }}
    .nav a {{
      display: inline-flex;
      align-items: center;
      min-height: 36px;
      margin-right: 8px;
      padding: 0 12px;
      border: 1px solid var(--line);
      border-radius: 999px;
      background: rgba(255, 253, 248, .84);
      color: var(--ink);
      text-decoration: none;
      font-size: .9rem;
    }}
    main {{
      max-width: 740px;
      margin: 38px auto 0;
    }}
    main > h1 {{ display: none; }}
    main > blockquote:first-child {{ display: none; }}
    h2 {{
      margin: 54px 0 16px;
      font-size: clamp(1.45rem, 3.4vw, 2.05rem);
      line-height: 1.28;
      text-wrap: pretty;
    }}
    p {{ margin: 0 0 18px; font-size: 1.035rem; }}
    ul {{ margin: 0 0 22px 1.1em; padding: 0; }}
    li {{ margin: 7px 0; }}
    strong {{ color: #1f4f4a; }}
    blockquote {{
      margin: 22px 0 28px;
      padding: 16px 18px;
      border-left: 4px solid var(--teal);
      background: var(--soft-teal);
      border-radius: 0 8px 8px 0;
      color: #34413c;
    }}
    .section-figure {{
      max-width: 900px;
      width: min(900px, calc(100vw - 44px));
      margin: 24px 50% 34px;
      transform: translateX(-50%);
    }}
    .section-figure img {{
      display: block;
      width: 100%;
      aspect-ratio: 16 / 9;
      object-fit: contain;
      background: var(--paper);
      border: 1px solid var(--line);
      border-radius: 12px;
      box-shadow: var(--shadow);
      cursor: zoom-in;
    }}
    .appendix {{
      max-width: 920px;
      margin: 58px auto 0;
      border-top: 1px solid var(--line);
      padding-top: 28px;
    }}
    .appendix details {{
      border: 1px solid var(--line);
      border-radius: 12px;
      background: rgba(255,253,248,.78);
      box-shadow: 0 10px 30px rgba(58, 50, 38, .08);
      overflow: hidden;
    }}
    .appendix summary {{
      cursor: pointer;
      padding: 18px 20px;
      font-weight: 800;
      color: var(--teal);
    }}
    .appendix-body {{
      max-height: 70vh;
      overflow: auto;
      padding: 0 20px 22px;
      border-top: 1px solid var(--line);
      background: #fffefa;
    }}
    .appendix-body p {{
      margin: 14px 0;
      font-size: .94rem;
      line-height: 1.62;
    }}
    .lightbox {{
      display: none;
      position: fixed;
      inset: 0;
      z-index: 200;
      background: rgba(26, 24, 21, .9);
      align-items: center;
      justify-content: center;
      padding: 24px;
      cursor: zoom-out;
    }}
    .lightbox.is-open {{ display: flex; }}
    .lightbox img {{
      max-width: 96vw;
      max-height: 92vh;
      width: auto;
      height: auto;
      border-radius: 8px;
      box-shadow: 0 12px 48px rgba(0,0,0,.42);
    }}
    .lightbox-hint {{
      position: absolute;
      top: 20px;
      right: 24px;
      color: rgba(255,255,255,.76);
      font-size: 14px;
    }}
    @media (max-width: 640px) {{
      .shell {{ padding: 20px 16px 56px; }}
      header {{ text-align: left; padding-top: 6px; }}
      h1 {{ font-size: clamp(1.82rem, 8.2vw, 2.12rem); line-height: 1.16; }}
      .meta {{ justify-content: flex-start; }}
      .nav {{ margin: 0 -16px; padding: 9px 16px; }}
      main {{ margin-top: 30px; }}
      h2 {{ margin-top: 44px; }}
      .summary-figure {{ max-width: 390px; margin-bottom: 28px; }}
      .summary-figure img {{ aspect-ratio: 9 / 16; max-width: 360px; }}
      .section-figure {{ width: calc(100vw - 32px); margin-top: 22px; margin-bottom: 28px; }}
      .section-figure img {{ aspect-ratio: 9 / 16; }}
      .appendix-body {{ max-height: 68vh; padding-inline: 16px; }}
    }}
  </style>
</head>
<body>
  <div class="shell">
    <header>
      <p class="eyebrow">Deep Guide｜AI、工作與能動性</p>
      <h1>{html.escape(title)}</h1>
      {figure_html(SUMMARY_FIGURE, "summary-figure")}
      <p class="dek">從李飛飛與 David Rogier 的對談出發，拆解 AI 兩極敘事、未來工作、教育重設、雙峰人才結構與空間智慧。</p>
      <ul class="meta">
        <li>Silicon Valley Girl Podcast</li>
        <li>2026 年 6 月 19 日</li>
        <li>Fei-Fei Li × David Rogier</li>
      </ul>
    </header>
    <nav class="nav" aria-label="章節導覽">{nav}<a href="#transcript">逐字稿</a></nav>
    <main>{body}</main>
    {appendix}
  </div>
  <div class="lightbox" id="lightbox">
    <span class="lightbox-hint">點擊或按 Esc 關閉</span>
    <img src="" alt="">
  </div>
  <script>
    (function(){{
      var lightbox = document.getElementById("lightbox");
      var lightboxImg = lightbox.querySelector("img");
      function openLightbox(img){{
        lightboxImg.src = img.currentSrc || img.src;
        lightboxImg.alt = img.alt;
        lightbox.classList.add("is-open");
      }}
      function closeLightbox(){{
        lightbox.classList.remove("is-open");
        lightboxImg.src = "";
      }}
      document.querySelectorAll("figure.summary-figure img, figure.section-figure img").forEach(function(img){{
        img.addEventListener("click", function(){{ openLightbox(img); }});
      }});
      lightbox.addEventListener("click", closeLightbox);
      document.addEventListener("keydown", function(e){{ if (e.key === "Escape") closeLightbox(); }});
    }})();
  </script>
</body>
</html>
"""


def main() -> None:
    md_text = NORMALIZED_MD.read_text(encoding="utf-8") if NORMALIZED_MD.exists() else SOURCE_MD.read_text(encoding="utf-8")
    main_md, appendix_md = split_markdown(md_text)
    title, prepared, sections = prepare_sections(main_md)
    body = markdown.markdown(prepared, extensions=["tables", "fenced_code", "attr_list"])
    body = re.sub(r"\A<h1[^>]*>.*?</h1>\s*", "", body, count=1, flags=re.S)
    body = inject_figures(body)
    appendix = render_appendix(appendix_md)
    OUT_HTML.write_text(render_page(title, body, appendix, sections), encoding="utf-8")
    print(OUT_HTML)


if __name__ == "__main__":
    main()
