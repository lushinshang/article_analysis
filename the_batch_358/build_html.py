import re
import markdown
import os

md_file = "guide.normalized.md"
with open(md_file, "r", encoding="utf-8") as f:
    content = f.read()

# 拆分原始文章的部分
parts = content.split("# 原始文章內容整理")
main_content = parts[0]
raw_content = "# 原始文章內容整理" + parts[1] if len(parts) > 1 else ""

html_main = markdown.markdown(main_content, extensions=['toc', 'fenced_code', 'tables'])
html_raw = markdown.markdown(raw_content, extensions=['toc', 'fenced_code', 'tables'])

# 插入 Summary 圖 (在第一段內容之前)
summary_html = """
<figure class="summary-figure">
  <picture>
    <source media="(max-width: 640px)" srcset="images/summary-mobile.png">
    <img src="images/summary.png" alt="文章重點總覽">
  </picture>
  <figcaption>一圖看懂：The Batch 358 核心觀點總覽</figcaption>
</figure>
"""

# 在第一個 h2 之前插入 summary
html_main = html_main.replace("<h2>一、", summary_html + "\n<h2>一、", 1)

# 插入 Mechanism 圖 (在第二段內容中)
mech_html = """
<figure class="section-figure">
  <picture>
    <source media="(max-width: 640px)" srcset="images/fable_mechanism-mobile.png">
    <img src="images/fable_mechanism.png" alt="Claude Fable 黑盒防禦機制圖">
  </picture>
  <figcaption>Claude Fable 5 的雙層過濾與降級路由機制</figcaption>
</figure>
"""

# 尋找 "黑盒防禦的稽核死局"
html_main = html_main.replace("這種「隱形降級」導致獨立評測機構", mech_html + "\n<p>這種「隱形降級」導致獨立評測機構", 1)

css = """
:root {
  --bg: #f9f7f4;
  --text: #1a1a1a;
  --accent: #0f172a;
  --link: #2563eb;
  --muted: #64748b;
  --border: #e2e8f0;
}
body {
  margin: 0;
  padding: 0;
  background: var(--bg);
  color: var(--text);
  font-family: "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
  line-height: 1.68;
  font-size: 17px;
  letter-spacing: 0;
  -webkit-font-smoothing: antialiased;
}
.container {
  max-width: 1120px;
  margin: 0 auto;
  padding: 0 24px;
}
article {
  max-width: 720px;
  margin: 0 auto 120px;
}
h1, h2, h3 {
  color: var(--accent);
  text-wrap: balance;
  line-height: 1.3;
}
h1 {
  font-size: clamp(2rem, 5vw, 3.2rem);
  margin-top: 64px;
  margin-bottom: 24px;
  font-weight: 800;
}
h2 {
  font-size: 1.75rem;
  margin-top: 48px;
  margin-bottom: 16px;
  border-bottom: 1px solid var(--border);
  padding-bottom: 8px;
}
h3 {
  font-size: 1.25rem;
  margin-top: 32px;
}
p {
  margin-bottom: 24px;
}
a {
  color: var(--link);
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}
hr {
  border: 0;
  border-top: 1px solid var(--border);
  margin: 48px 0;
}
figure {
  margin: 48px 0;
  text-align: center;
}
figure.section-figure {
  width: 100%;
}
figure picture {
  display: block;
}
figure.summary-figure {
  margin: 32px 0;
  padding: 0;
}
figure.summary-figure img {
  width: 100%;
  max-width: 640px;
  display: block;
  margin: 0 auto;
  border-radius: 12px;
  aspect-ratio: 16 / 9;
  object-fit: cover;
  box-shadow: 0 6px 24px rgba(0,0,0,0.08);
}
figure.section-figure img {
  width: 100%;
  height: auto;
  display: block;
  margin: 0 auto;
  border-radius: 14px;
  aspect-ratio: 16 / 9;
  object-fit: contain;
  background: #f7f0dc;
  box-shadow: 0 12px 36px rgba(7,21,33,0.18);
}
figcaption {
  margin-top: 12px;
  font-size: 14px;
  color: var(--muted);
  line-height: 1.54;
}
pre {
  background: #1e293b;
  color: #f8fafc;
  padding: 16px;
  border-radius: 8px;
  overflow-x: auto;
  font-size: 14px;
}
code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
}
@media (max-width: 640px) {
  figure.summary-figure img {
    aspect-ratio: 16 / 9;
    max-width: none;
    object-fit: contain;
  }
  figure.section-figure {
    width: 100%;
    margin-top: 36px;
    margin-bottom: 36px;
  }
  figure.section-figure img {
    aspect-ratio: 16 / 9;
    border-radius: 12px;
  }
  figcaption {
    padding: 0 16px;
  }
  body { font-size: 16px; }
}

/* Lightbox */
figure.summary-figure img, figure.section-figure img { cursor: zoom-in; }
.lightbox {
  display: none; position: fixed; inset: 0; z-index: 200;
  background: rgba(26,26,26,0.88);
  align-items: center; justify-content: center; padding: 24px;
  cursor: zoom-out;
}
.lightbox.is-open { display: flex; }
.lightbox img {
  max-width: 96vw; max-height: 92vh; width: auto; height: auto;
  border-radius: 8px; box-shadow: 0 12px 48px rgba(0,0,0,0.4);
}
.lightbox .lightbox-hint { position: absolute; top: 20px; right: 24px; color: rgba(255,255,255,0.75); font-size: 14px; }
"""

html_template = f"""<!DOCTYPE html>
<html lang="zh-Hant-TW">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>掌控權的幽靈：從 Claude Fable 的「隱形降級」看 AI 時代的供應鏈主權與防禦邊界</title>
  <style>
{css}
  </style>
</head>
<body>
  <div class="container">
    <article>
      {html_main}
      <hr>
      {html_raw}
    </article>
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
      function closeLightbox(){{ lightbox.classList.remove("is-open"); lightboxImg.src = ""; }}
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

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)
