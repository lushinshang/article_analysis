from pathlib import Path
import re

import markdown
from bs4 import BeautifulSoup


BASE = Path(__file__).resolve().parent
MD_FILE = BASE / "World_Labs'_Fei-Fei_Li_on_Creating_Large_World_Models_次主題深度導讀.md"
HTML_FILE = BASE / "world_labs_fei_fei_li_large_world_models.html"


def slugify(text: str) -> str:
    slug = re.sub(r"[^\w\u4e00-\u9fff]+", "-", text.lower()).strip("-")
    return slug or "section"


def add_section_ids(soup: BeautifulSoup) -> list[tuple[str, str, int]]:
    used: dict[str, int] = {}
    nav_items: list[tuple[str, str, int]] = []
    for heading in soup.find_all(["h2", "h3"]):
        title = heading.get_text(" ", strip=True)
        base = slugify(title)
        count = used.get(base, 0)
        used[base] = count + 1
        ident = base if count == 0 else f"{base}-{count + 1}"
        heading["id"] = ident
        level = int(heading.name[1])
        if level == 2 or title.startswith("次主題"):
            nav_items.append((ident, title, level))
    return nav_items


def enhance_images(soup: BeautifulSoup) -> None:
    for img in list(soup.find_all("img")):
        alt = img.get("alt", "").strip()
        img["loading"] = "lazy"
        img["decoding"] = "async"
        img["class"] = img.get("class", []) + ["article-image"]
        figure = soup.new_tag("figure", **{"class": "image-figure"})
        caption = soup.new_tag("figcaption")
        caption.string = alt
        img.wrap(figure)
        figure.append(caption)
    for p in list(soup.find_all("p")):
        children = [child for child in p.contents if getattr(child, "name", None) or str(child).strip()]
        if len(children) == 1 and getattr(children[0], "name", None) == "figure":
            p.replace_with(children[0].extract())


def wrap_content_sections(soup: BeautifulSoup) -> None:
    body = soup.body or soup
    article = soup.new_tag("article", **{"class": "article"})
    nodes = list(body.contents)
    for node in nodes:
        article.append(node.extract())
    body.append(article)

    for h2 in article.find_all("h2"):
        text = h2.get_text(" ", strip=True)
        if text == "摘要":
            h2["class"] = h2.get("class", []) + ["summary-heading"]
        if text == "可讀版逐字稿":
            h2["class"] = h2.get("class", []) + ["transcript-heading"]
            parent = soup.new_tag("section", **{"class": "transcript-section"})
            h2.wrap(parent)
            cursor = parent.next_sibling
            while cursor:
                nxt = cursor.next_sibling
                parent.append(cursor.extract())
                cursor = nxt
            break


def build_html(md_text: str) -> str:
    html_body = markdown.markdown(
        md_text,
        extensions=["extra", "sane_lists", "smarty", "toc"],
        output_format="html5",
    )
    soup = BeautifulSoup(f"<main>{html_body}</main>", "html.parser")
    nav_items = add_section_ids(soup)
    enhance_images(soup)
    wrap_content_sections(soup)

    nav_links = "\n".join(
        f'<a href="#{ident}" class="nav-link level-{level}">{title}</a>'
        for ident, title, level in nav_items
    )

    return f"""<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>World Labs 的 Fei-Fei Li 談 Large World Models｜次主題深度導讀</title>
  <meta name="description" content="Fei-Fei Li 談大型世界模型、Spatial Intelligence、機器人、AI 安全、教育與 AGI 的訪談次主題深度導讀。">
  <style>
    :root {{
      --bg: #f7f3ec;
      --paper: #fffdf8;
      --ink: #24211d;
      --muted: #686058;
      --line: #e5dacb;
      --accent: #1f6f68;
      --accent-soft: #e3f1ed;
      --accent-strong: #174f4a;
      --code-bg: #f0eadf;
      --shadow: 0 18px 55px rgba(60, 44, 25, 0.10);
    }}

    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
      color: var(--ink);
      background:
        radial-gradient(circle at 8% 0%, rgba(31, 111, 104, 0.08), transparent 30rem),
        linear-gradient(180deg, #fbf7f0 0%, var(--bg) 34rem);
      letter-spacing: 0;
    }}
    a {{ color: var(--accent-strong); text-decoration-thickness: 1px; text-underline-offset: 0.16em; }}
    .topbar {{
      position: sticky;
      top: 0;
      z-index: 10;
      border-bottom: 1px solid rgba(229, 218, 203, 0.88);
      background: rgba(255, 253, 248, 0.92);
      backdrop-filter: blur(14px);
    }}
    .nav {{
      max-width: 1120px;
      margin: 0 auto;
      padding: 0.72rem 1.25rem;
      display: flex;
      gap: 0.55rem;
      overflow-x: auto;
      scrollbar-width: thin;
    }}
    .nav-link {{
      flex: 0 0 auto;
      padding: 0.42rem 0.68rem;
      border: 1px solid var(--line);
      border-radius: 999px;
      background: #fffaf0;
      color: #51483f;
      font-size: 0.86rem;
      text-decoration: none;
      white-space: nowrap;
    }}
    .nav-link:hover {{
      border-color: rgba(31, 111, 104, 0.45);
      color: var(--accent-strong);
      background: var(--accent-soft);
    }}
    .page {{
      max-width: 1120px;
      margin: 0 auto;
      padding: 4.3rem 1.25rem 5rem;
    }}
    .article {{
      max-width: 760px;
      margin: 0 auto;
      background: rgba(255, 253, 248, 0.74);
      border: 1px solid rgba(229, 218, 203, 0.78);
      border-radius: 18px;
      box-shadow: var(--shadow);
      padding: 3.5rem 3.3rem;
    }}
    h1 {{
      margin: 0 0 1.25rem;
      font-size: clamp(2.15rem, 5vw, 3.45rem);
      line-height: 1.08;
      text-wrap: balance;
      color: #181512;
    }}
    h2 {{
      margin: 3.2rem 0 1rem;
      padding-top: 0.35rem;
      font-size: clamp(1.55rem, 3vw, 2.08rem);
      line-height: 1.26;
      text-wrap: balance;
      color: #1e1a16;
    }}
    h3 {{
      margin: 2.25rem 0 0.75rem;
      font-size: 1.25rem;
      line-height: 1.35;
      color: #2b2621;
    }}
    p, li {{ font-size: 1.03rem; line-height: 1.72; }}
    p {{ margin: 0 0 1.12rem; }}
    strong {{ color: #211d19; font-weight: 700; }}
    blockquote {{
      margin: 1.4rem 0 2rem;
      padding: 1.05rem 1.25rem;
      border-left: 4px solid var(--accent);
      border-radius: 0 10px 10px 0;
      background: var(--accent-soft);
      color: #36534f;
    }}
    blockquote p {{ margin: 0; }}
    hr {{ margin: 2.75rem 0; border: 0; border-top: 1px solid var(--line); }}
    code {{
      padding: 0.12rem 0.34rem;
      border-radius: 5px;
      background: var(--code-bg);
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
      font-size: 0.92em;
    }}
    .summary-heading + p,
    .summary-heading + p + p,
    .summary-heading + p + p + p {{ font-size: 1.08rem; }}
    .article > p:nth-of-type(-n+4) {{ color: var(--muted); }}
    .image-figure {{
      width: min(860px, calc(100vw - 2.5rem));
      margin: 2.25rem 50% 2.5rem;
      transform: translateX(-50%);
    }}
    .article-image {{
      display: block;
      width: 100%;
      aspect-ratio: 16 / 9;
      object-fit: contain;
      border-radius: 14px;
      border: 1px solid var(--line);
      background: #fffaf0;
      box-shadow: 0 14px 38px rgba(60, 44, 25, 0.12);
    }}
    figcaption {{
      margin-top: 0.65rem;
      color: var(--muted);
      font-size: 0.92rem;
      line-height: 1.55;
      text-align: center;
    }}
    .transcript-section {{
      margin: 3.6rem -1.25rem -1.25rem;
      padding: 2rem 1.25rem 1.25rem;
      border-radius: 16px;
      background: #f3ecdf;
      border: 1px solid var(--line);
    }}
    .transcript-section h2 {{ margin-top: 0; }}
    .transcript-section h3 {{
      margin-top: 2rem;
      padding-top: 1.5rem;
      border-top: 1px solid rgba(104, 96, 88, 0.18);
      color: var(--accent-strong);
    }}
    .transcript-section p {{ font-size: 0.98rem; line-height: 1.68; color: #403a33; }}
    .transcript-section p:nth-of-type(2n + 4) {{
      padding-left: 1rem;
      border-left: 2px solid rgba(31, 111, 104, 0.25);
    }}
    @media (max-width: 760px) {{
      .page {{ padding: 2.1rem 0.85rem 3rem; }}
      .article {{ padding: 2rem 1.05rem; border-radius: 12px; }}
      .nav {{ padding: 0.62rem 0.85rem; }}
      h1 {{ font-size: 2.08rem; }}
      p, li {{ font-size: 1rem; line-height: 1.68; }}
      .image-figure {{ width: calc(100vw - 1.7rem); margin-top: 1.75rem; margin-bottom: 2rem; }}
      .transcript-section {{
        margin-left: -0.35rem;
        margin-right: -0.35rem;
        padding-left: 0.85rem;
        padding-right: 0.85rem;
      }}
    }}
  </style>
</head>
<body>
  <header class="topbar">
    <nav class="nav" aria-label="章節導覽">
      {nav_links}
    </nav>
  </header>
  <div class="page">
    {soup.main.decode_contents()}
  </div>
</body>
</html>
"""


def main() -> None:
    HTML_FILE.write_text(build_html(MD_FILE.read_text(encoding="utf-8")), encoding="utf-8")
    print(HTML_FILE)


if __name__ == "__main__":
    main()
