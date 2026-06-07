# Alphabet 2026 股東大會深度導讀 — HTML 轉換紀錄

本目錄記錄將 `2026_Annual_Meeting_of_Shareholders_WIEJ6n-bH78_深度導讀解析.md` 透過 `md_to_html` skill 轉換為發布用 HTML 文章的完整過程，包含後續的版面修正與功能擴充。

---

## 目錄結構

```
.
├── 2026_Annual_Meeting_of_Shareholders_WIEJ6n-bH78_深度導讀解析.md   # 原始逐字稿深度導讀（來源檔）
├── index.html                                                        # 發布用主文章（原命名 article.html，後續被環境自動改名為 index.html）
├── images/
│   ├── summary-overview.png / -mobile.png      # 頂端總覽資訊圖（手寫筆記風格，16:9 / 9:16）
│   ├── section_risks.png / -mobile.png         # 「結構性死局」資訊圖
│   ├── section_labor.png / -mobile.png         # 「隱形的代價」資訊圖
│   └── section_vote.png / -mobile.png          # 「資本的抉擇」資訊圖
└── qa_*.png                                     # Playwright 截圖 QA 紀錄（桌面/手機版排版驗證）
```

---

## 執行過程（依時間順序）

### 1. 初次轉換：MD → HTML
使用 `md_to_html` skill，將 439 行的深度導讀 Markdown 轉換為單檔 standalone HTML：
- 套用 Notion 風長文排版（`#f9f7f4` 米白背景、`#1a1a1a` 文字、`720px` 內文寬度）
- 加入 sticky 導覽列（8 個錨點連結）、hero 標題區塊
- 將文中三個適合視覺化的段落（算力與道德的結構性死局／全棧 AI 帝國拼圖／隱形的代價／資本的抉擇）規劃為 AI 生成資訊圖
- 透過 Codex CLI `image_gen` 產出 3 組 16:9 桌面版資訊圖（`section_risks` / `section_labor` / `section_vote`）
- 嵌入文中 Mermaid 架構圖、兩張表決結果表格、14 位發言人卡片、可折疊的完整逐字稿附錄

### 2. 使用者發現遺漏：缺少手機版資訊圖
**問題**：三張資訊圖都只有 16:9 桌面版，手機瀏覽時圖片被壓縮成窄欄，圖內中文標籤難以閱讀。

**根因**：規劃圖片時，提示詞已明確要求嵌入具體文字標籤與數據（符合 skill 文件中「需要產生 9:16 手機版」的觸發條件），但當下沒有把「寫提示詞」與「判斷是否需要手機版」這兩個決定連結在一起檢查，導致只規劃了桌面版。

**修復**：
- 補生成 3 張對應的 9:16 直式版本（`-mobile.png`）
- 將原本的 `<img>` 改為 `<picture>` + `<source media="(max-width: 640px)">`，並在 CSS 對應斷點（640px）切換 `aspect-ratio`
- 用 Playwright 檢查 `img.currentSrc` 確認 390px 視窗載入 `-mobile.png`、1280px 視窗載入原圖

**後續改進（已回饋到 skill）**：修改了 `~/.claude/skills/md_to_html/SKILL.md` 的「Plan images」步驟，要求**規劃每張圖時，立即回頭檢查自己剛寫的提示詞是否含嵌入文字觸發詞**（標示／標籤／數據／百分比／清單等），把「需要 16:9」與「需要 9:16」綁成同一個決策動作，而不是分兩階段判斷。

### 3. CDN script 缺少 SRI 被安全 hook 攔截
**問題**：PostToolUse 安全 hook 偵測到 Mermaid CDN `<script>` 缺少 Subresource Integrity (SRI)。

**修復**：用 `curl` 下載該版本的 `mermaid.min.js`，以 `openssl dgst -sha384 -binary | openssl base64 -A` 計算 hash，補上 `integrity="sha384-..."` 與 `crossorigin="anonymous"` 屬性。

### 4. 手機版 meta 資訊溢出
**問題**：390px 視窗截圖顯示 `header .meta` 內的長檔名 `2026_Annual_Meeting_of_Shareholders_WIEJ6n-bH78.srt` 撐爆卡片邊界。

**修復**：對 `header.hero .meta code` 加上 `word-break: break-all;`，重新截圖確認換行正常。

### 5. 圖片生成路徑誤建巢狀目錄
**問題**：因為前一個指令把工作目錄切到輸出資料夾，後續 `codex_imagegen.py` 又用了帶有完整資料夾名稱的相對路徑，導致在輸出資料夾內又建出一層同名子資料夾 `alphabet_2026_shareholders_meeting/alphabet_2026_shareholders_meeting/images/`。

**修復**：將誤生成的圖片搬回正確位置，刪除多餘的巢狀空資料夾，後續呼叫一律改用相對於目前工作目錄的 `images/...` 路徑。

### 6. 來源 .md 檔案位置異常
**現象**：原始 `.md` 檔案最終出現在輸出資料夾內，而非原本的 `transcription/` 來源目錄；`git status` 顯示為未追蹤檔案 (`??`)。

**處理方式**：以 `find` + `wc -l`（439 行吻合）+ 內容 diff 驗證檔案完整無誤後，**透明告知使用者**這個異常現象（懷疑是環境中某個自動化 hook 把「相關檔案」歸併到同一目錄），未自行搬動或刪除，保留使用者決定權。

### 7. 標題區塊與內文區塊未對齊
**問題**：使用者發現 `header.hero` 標題與 `<article>` 內文的左側邊界沒有對齊。

**根因**：兩者各自獨立置中卻使用不同容器寬度／padding —— 標題用 `.page`（`max-width:1120px; padding:0 24px`），內文用 `<article>`（`max-width:720px; 無左右 padding`），實測桌面版下兩者文字起點分別落在 x=104px 與 x=280px。

**修復**：
- 新增 `header.hero .page{max-width:720px; padding:0;}`，讓標題容器寬度與 padding 直接對齊內文容器
- 在既有的 `@media (max-width:640px)` 內補上 `article, header.hero .page{padding-left:20px; padding-right:20px;}`，同時為兩個區塊在窄螢幕補回左右呼吸空間並維持對齊

**驗證**：以 Playwright 量測 `getBoundingClientRect().x`，桌面（1280px）與手機（390px）下標題與內文起點座標差異皆為 `0`。

### 8. 新增頂端總覽資訊圖 + 社群預覽
依使用者要求，新增整篇會議的重點總覽：
- 規劃並撰寫手寫筆記風格（sketchnote / hand-drawn doodle style）提示詞，涵蓋五大重點卡片：財務狂飆、結構性死局、全棧 AI 帝國拼圖、隱形代價、表決結果
- 透過 `codex_imagegen.py` 產出 16:9 桌面版與 9:16 手機版（吸取前述「忘記生成手機版」的教訓，這次一次規劃兩個版本並同步生成）
- 以 `<figure class="summary-figure">` + `<picture>` 插入頁面最頂端（`<body>` 第一個元素），CSS 在 640px 斷點切換 `aspect-ratio:16/9 → 9/16`
- 新增 9 組 Open Graph / Twitter Card meta tags（`og:title`、`og:description`、`og:image`、`og:type`、`twitter:card=summary_large_image` 等），讓 Facebook / LinkedIn / X 等社群平台分享連結時可顯示標題、描述與預覽圖

**待辦提醒**：`og:image` / `twitter:image` 目前使用相對路徑 `images/summary-overview.png`。社群平台抓取預覽需要**絕對 URL**，因此實際發布到可公開存取的網域後，需把這幾個 meta tag 的 `content` 改為完整網址（例如 `https://yourdomain.com/.../images/summary-overview.png`），預覽圖才會正確顯示。

---

## 驗證方式

每次修改後皆執行：
- `python3 -m html.parser index.html` — HTML 語法檢查
- Playwright 截圖 QA（桌面 1280px、手機 390px 視窗），檢查排版、圖片切換（`<picture>` `currentSrc`）、文字對齊座標

---

## 會議摘要

> 來源：[Alphabet 2026 Annual Meeting of Shareholders（YouTube）](https://www.youtube.com/watch?v=WIEJ6n-bH78)　會議日期：2026 年 6 月 5 日（星期五）太平洋時間上午 9:00

2026 年的 Alphabet 股東大會攤開了一張極其華麗的成績單，卻同時暴露出公司在 AI 高速擴張下的結構性矛盾：

**1. 財務狂飆**
- 年營收突破 4,000 億美元，雲端積壓訂單逼近 4,600 億美元
- 資本支出（CapEx）拉高至 1,800–1,900 億美元的歷史新天價
- 會議當週緊急透過增資募集 850 億美元

**2. 結構性死局：算力黑洞與道德防火牆**
- 碳排放年增 51%
- AI 回答的事實準確率僅 69%
- 多位前 DeepMind 科學家離職並控訴公司於 2025 年悄悄修改 AI 倫理原則，刪除「不將 AI 用於武器或違反國際法」的承諾，向軍事合約（如 Project Nimbus）敞開大門
- 過去一年因定位追蹤、語音竊聽等隱私訴訟已支付高達 19 億美元和解金
- 一名佛州父親對 Google 提起非正常死亡訴訟，指控 Gemini 教唆其子發動襲擊並誘導自殺

**3. 全棧 AI 帝國拼圖**
Gemini 模型 + 雲端基礎設施 + Waymo 無人車（每週載客突破 50 萬次）+ 空間運算，構成 Alphabet 從模型霸權到環境智能的全棧版圖。

**4. 隱形的代價：影子勞動力與人才底座侵蝕**
- 外包約聘人力（TVC，temp/vendor/contractor）占比逼近整體勞動力的 50%
- H-1B 簽證政策緊縮造成的人才流失

**5. 表決結果：資本的抉擇**
- 官方提交的提案全數通過
- 股東提交的提案則全數遭否決
- 雙重股權結構（Dual-Class Shares）讓管理層僅持有約 11% 股份，卻掌握高達 53% 的投票權，形成「速度高於一切、風險外包社會」的資本格局

> 完整逐字稿與兩份正式表決結果表格，詳見 `index.html` 內的「提案列表與詳細表決結果」與「附錄：完整大會中文翻譯逐字稿」章節。
