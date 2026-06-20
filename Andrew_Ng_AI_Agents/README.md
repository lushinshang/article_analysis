# Andrew Ng：AI Agents 時代的軟體工程革命

本目錄收錄 Andrew Ng 在 Interrupt 26 訪談的繁體中文深度導讀、發布版 HTML、資訊圖表、生圖規格及畫面驗證結果。

## 快速開啟

主要成果：

- [`index.html`](./index.html)：可直接用瀏覽器開啟的發布版頁面
- [`andrew_ng_agents_deep_guide.md`](./andrew_ng_agents_deep_guide.md)：深度導讀 Markdown 原稿

若瀏覽器限制本機影片或資源載入，可在專案根目錄啟動本機伺服器：

```bash
python3 -m http.server 8766
```

然後開啟：

```text
http://127.0.0.1:8766/transcription/deepguide_Andrew_Ng_AI_Agents/index.html
```

## 目錄結構

```text
deepguide_Andrew_Ng_AI_Agents/
├── README.md
├── index.html
├── andrew_ng_agents_deep_guide.md
├── IMAGE_GENERATION_PLAN.md
├── PROMPTS_FOR_CODEX_CLI.md
├── images/
│   ├── summary_infographic_16x9.png
│   ├── summary_infographic_9x16.png
│   ├── context_hub_flow_16x9.png
│   ├── context_hub_flow_9x16.png
│   ├── organization_shift_16x9.png
│   ├── organization_shift_9x16.png
│   ├── pigeonhole_principle_16x9.png
│   ├── bank_loan_flow_16x9.png
│   ├── bank_loan_flow_9x16.png
│   ├── lego_metaphor_16x9.png
│   ├── lego_metaphor_9x16.png
│   ├── open_source_timeline_16x9.png
│   └── fde_analysis_16x9.png
└── qa-*.png
```

## 各檔案用途

### `index.html`

最終發布頁面，包含：

- 頂部 HTML5 影片播放器
- 影片最大寬度 `860px`，行動版依螢幕寬度縮放
- 影片時間碼點擊跳轉
- 章節導覽列
- 13 張 PNG 資訊圖表
- 桌面版 16:9、行動版 9:16 自動切換
- 點擊圖片放大的 Lightbox
- `Esc` 或點擊背景關閉 Lightbox
- 完整深度導讀及訪談逐字內容

影片來源：

```text
https://github.com/lushinshang/article_analysis/releases/download/article_mv/The.Future.of.AI.Agents.with.Andrew.Ng.Interrupt.26.mp4
```

### `andrew_ng_agents_deep_guide.md`

文章內容原稿。修改核心論述、段落或逐字稿時，應先更新此檔，再同步到 `index.html`。

### `IMAGE_GENERATION_PLAN.md`

資訊圖表整體規劃，包括：

- 圖片位置
- 圖片主題與優先順序
- 16:9／9:16 版本需求
- HTML 影片播放器規格
- Lightbox 與時間軸互動規劃

### `PROMPTS_FOR_CODEX_CLI.md`

每張資訊圖表的詳細生圖提示詞。重新生圖時，以此檔為主要內容規格。

### `images/`

HTML 實際引用的 PNG 圖片。所有圖片由 `codex exec` 呼叫內建 `image_gen` 生成，不是 SVG 轉檔。

### `qa-*.png`

桌面版及行動版的畫面驗證截圖。這些檔案不會被正式 HTML 引用，可在需要重新驗證版面時更新或清除。

## 圖片清單

| 主題 | 桌面版 | 行動版 |
|---|---|---|
| 全文摘要 | `summary_infographic_16x9.png` | `summary_infographic_9x16.png` |
| Context Hub 流程 | `context_hub_flow_16x9.png` | `context_hub_flow_9x16.png` |
| 組織結構轉變 | `organization_shift_16x9.png` | `organization_shift_9x16.png` |
| 鴿籠原理 | `pigeonhole_principle_16x9.png` | 無 |
| 銀行貸款流程 | `bank_loan_flow_16x9.png` | `bank_loan_flow_9x16.png` |
| LEGO 積木比喻 | `lego_metaphor_16x9.png` | `lego_metaphor_9x16.png` |
| 開源模型時間軸 | `open_source_timeline_16x9.png` | 無 |
| FDE 角色分析 | `fde_analysis_16x9.png` | 無 |

圖片尺寸：

- 16:9：`1672 × 941`
- 9:16：`941 × 1672`
- 格式：PNG、RGB

沒有行動版的三張圖片會在手機上維持完整 16:9 比例，不裁切資訊內容。

## HTML 圖片切換方式

有行動版的圖片使用 `<picture>`：

```html
<picture>
  <source
    media="(max-width: 768px)"
    srcset="images/context_hub_flow_9x16.png"
  >
  <img
    src="images/context_hub_flow_16x9.png"
    alt="Context Hub 掃描、注入、決策與反饋的四步流程"
  >
</picture>
```

若新增一組桌面／行動圖片，必須同時：

1. 把兩張 PNG 放入 `images/`
2. 在 HTML 加入 `<picture>` 與 `<source>`
3. 為外層 `<figure>` 加上 `has-mobile`
4. 提供清楚的 `alt` 與 `figcaption`
5. 確認 Lightbox 使用 `img.currentSrc`

## 重新生圖

建議使用 `codex exec`，讓子 Codex 呼叫內建 `image_gen`：

```bash
codex exec --json -s workspace-write --skip-git-repo-check \
  "使用 imagegen skill，讀取
  transcription/deepguide_Andrew_Ng_AI_Agents/IMAGE_GENERATION_PLAN.md
  與 PROMPTS_FOR_CODEX_CLI.md，
  依指定提示詞生成真正的 PNG，
  並存入 transcription/deepguide_Andrew_Ng_AI_Agents/images/"
```

生圖要求：

- 必須使用 `imagegen` Skill 及內建 `image_gen`
- 輸出必須是實際 PNG，不可用 SVG、HTML 或 Canvas 代替
- 使用台灣繁體中文
- 視覺風格為粉圓體、kawaii 資訊圖表
- 背景以 `#f9f7f4` 米色為主
- 不得出現浮水印或無關品牌標誌
- 行動版必須保留桌面版的核心元素，而不是只生成相同主題的不同圖片

如果 `codex exec` 的圖片結果存在工作階段 JSONL，而未自動寫入 `generated_images/`，可從該次工作階段的 `image_generation_call.payload.result` 取出 Base64 PNG，再解碼到目標檔案。解碼後必須用 `file` 或 `sips` 驗證，不可只檢查副檔名。

## 驗證方式

### 驗證 HTML 語法

```bash
python3 -m html.parser \
  transcription/deepguide_Andrew_Ng_AI_Agents/index.html
```

### 驗證 PNG 格式及尺寸

```bash
file transcription/deepguide_Andrew_Ng_AI_Agents/images/*.png

for image in transcription/deepguide_Andrew_Ng_AI_Agents/images/*.png; do
  echo "$image"
  sips -g pixelWidth -g pixelHeight -g format "$image"
done
```

### 檢查 HTML 是否仍引用 SVG

```bash
rg 'images/.*\.svg' \
  transcription/deepguide_Andrew_Ng_AI_Agents/index.html
```

正常結果應為沒有輸出。

### 畫面 QA

桌面版建議檢查：

- 影片寬度不超過 `860px`
- 摘要圖使用 16:9
- 文章圖片文字可辨識
- 圖片不超出文章容器

行動版建議檢查：

- 摘要、Context Hub、組織、銀行及 LEGO 使用 9:16 圖片
- 沒有水平捲動或文字重疊
- 導覽列可水平捲動
- Lightbox 顯示的是行動版 `currentSrc`

## 維護注意事項

- `index.html` 是目前正式入口，請勿重新建立舊檔名 `andrew_ng_agents_deep_guide.html`
- 圖片檔名已被 HTML 直接引用，重新生圖時應保留既有檔名
- 若修改圖片斷點，CSS 與 `<source media>` 必須使用相同寬度
- 資訊圖表包含文字，不要使用 `object-fit: cover`，避免裁切
- 修改 Lightbox 時必須保留 `currentSrc`，否則手機會放大錯誤的桌面圖片
- 圖片文字由生成模型繪製，重新生成後應人工檢查繁體中文、數字、箭頭方向及流程順序
- `.DS_Store` 為 macOS 系統檔，與發布內容無關

## 目前狀態

- HTML 入口：完成
- 影片播放器：完成
- 影片時間碼跳轉：完成
- PNG 資訊圖表：13 張完成
- 桌面／行動圖片切換：完成
- Lightbox：完成
- HTML 與圖片路徑驗證：完成
- 桌面及行動畫面 QA：完成

