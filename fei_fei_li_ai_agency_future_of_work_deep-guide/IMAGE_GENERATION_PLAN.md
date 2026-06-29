# Fei-Fei Li AI Agency Future of Work：Image Generation Plan

Use `imagegen` through `codex exec` to generate real PNG infographics. Do not create SVG, HTML, or placeholder images. Save all output files under:

`transcription/fei_fei_li_ai_agency_future_of_work_deep-guide/images/`

Visual style for every image:

- 台灣繁體中文資訊圖
- 粉圓體 / rounded Traditional Chinese typography
- refined kawaii infographic, not childish
- warm paper background `#f9f7f4`
- restrained accents: teal, coral, muted gold, ink gray
- crisp labels, clear arrows, no watermark, no unrelated logos
- all text must be readable
- 16:9 desktop image first, then a matching 9:16 mobile recomposition
- mobile version must preserve the same concrete elements and labels, stacked vertically

## Output List

| # | Topic | Desktop | Mobile |
|---|---|---|---|
| 1 | 全文摘要 | `summary.png` | `summary-mobile.png` |
| 2 | 使用者 vs 旁觀者差距 | `agency-gap.png` | `agency-gap-mobile.png` |
| 3 | 兩極敘事 vs 細緻中間路線 | `nuanced-middle.png` | `nuanced-middle-mobile.png` |
| 4 | 人類智慧能力地圖 | `human-intelligence-map.png` | `human-intelligence-map-mobile.png` |
| 5 | 產品經理工作流前後對照 | `pm-workflow.png` | `pm-workflow-mobile.png` |
| 6 | 雙峰人才結構 | `barbell-workers.png` | `barbell-workers-mobile.png` |
| 7 | 空間智慧與 agency 路徑 | `spatial-agency.png` | `spatial-agency-mobile.png` |

## Prompts

### 1A. summary.png 16:9

依據文章「從 AI 焦慮到個人能動性：李飛飛談未來十年的工作、教育與空間智慧」生成一張「一圖看懂」總覽資訊圖，台灣繁體中文，粉圓體，refined kawaii infographic，16:9。

版面：米白紙張背景，六張重點卡片，清楚標題「AI 時代的分水嶺：能動性」。每張卡片包含小圖示、短標籤、1 句重點。

六張卡片必須是：
1. 「不是烏托邦／末日論」：兩個極端泡泡，中間是「細緻中間路線」
2. 「AI 使用差距擴大」：一人用 AI 自建工具，另一人停在觀望
3. 「智慧不是單一商品」：語言、空間、身體、情感、創造力
4. 「工作被任務拆解」：職稱不是單位，任務才是單位
5. 「兩種工作者」：頂尖專家 + 高能動性通才
6. 「空間智慧」：理解、推理、生成、互動

底部標語：「不是會不會用工具，而是能不能把工具轉成責任」。

### 1B. summary-mobile.png 9:16

依據 1A 的原始 16:9 資訊圖內容，重新繪製成 9:16 直式版本，台灣繁體中文，粉圓體，refined kawaii infographic。

務必保留並重現：
- 大標題「AI 時代的分水嶺：能動性」
- 六張重點卡片垂直排列
- 卡片標籤：「不是烏托邦／末日論」、「AI 使用差距擴大」、「智慧不是單一商品」、「工作被任務拆解」、「兩種工作者」、「空間智慧」
- 底部標語：「不是會不會用工具，而是能不能把工具轉成責任」

### 2A. agency-gap.png 16:9

依據文章第一節生成資訊圖，主題是「AI 使用者與旁觀者的差距正在擴大」，台灣繁體中文，粉圓體，16:9。

畫面左右對比：
左側標題「旁觀者」：只問「哪個工具最好？」、停在焦慮與觀望、仍被現成軟體流程限制。
右側標題「高能動性使用者」：用 AI 自建小工具、重組工作流程、接上資料與責任鏈。
中間用逐漸拉開的距離箭頭，標籤「差距擴大」。

右側要包含 David 的待辦清單例子：卡片文字「待辦超過 1.5 天 → 立刻做／刪掉／委派」。
底部提醒：「能產生畫面 ≠ 能重組工作」。

### 2B. agency-gap-mobile.png 9:16

依據 2A 的原始 16:9 圖，重新繪製成 9:16 直式版本。

務必保留：
- 標題「AI 使用者與旁觀者的差距」
- 上方「旁觀者」卡片：焦慮、觀望、被工具限制
- 中間「差距擴大」箭頭
- 下方「高能動性使用者」卡片：自建工具、重組流程、接上資料與責任鏈
- 待辦清單例子：「超過 1.5 天 → 做／刪／委派」
- 底部提醒：「能產生畫面 ≠ 能重組工作」

### 3A. nuanced-middle.png 16:9

依據文章第二節生成資訊圖，主題是「AI 兩極敘事 vs 細緻中間路線」，台灣繁體中文，粉圓體，16:9。

畫面三欄：
左欄「烏托邦敘事」：AI 自動拯救世界、人類不用工作、忽略制度問題。
右欄「末日敘事」：AI 吞掉所有工作、個人只能被動、拒絕接觸工具。
中欄較大「細緻中間路線」：AI 是強大工具、理解能力邊界、用於增能、警覺風險與不公平。

中間欄要有四個問題小標籤：
「能做什麼？」、「哪裡脆弱？」、「如何增能？」、「風險在哪？」。

### 3B. nuanced-middle-mobile.png 9:16

依據 3A 的原始 16:9 圖，重新繪製成 9:16 直式版本。

務必保留：
- 標題「不要二選一：走進細緻中間路線」
- 上方兩個小卡：「烏托邦敘事」、「末日敘事」
- 中央大卡「細緻中間路線」
- 四個問題標籤：「能做什麼？」、「哪裡脆弱？」、「如何增能？」、「風險在哪？」

### 4A. human-intelligence-map.png 16:9

依據文章第三節生成資訊圖，主題是「人類智慧不是單一商品」，台灣繁體中文，粉圓體，16:9。

中心圓標題「人類智慧」。周圍六個能力節點，用清楚圖示與標籤：
1. 語言智慧：理解、表達、推理
2. 感知智慧：看見環境與異常
3. 空間智慧：物體、距離、方向
4. 身體智慧：操作、移動、協調
5. 情感智慧：信任、脈絡、關係
6. 創造力：經驗、價值、表達

旁邊放一個小型 LLM 圖示，標籤「語言能力很強，但不是全部智慧」。底部標語：「智慧成本歸零，是錯誤問題」。

### 4B. human-intelligence-map-mobile.png 9:16

依據 4A 的原始 16:9 圖，重新繪製成 9:16 直式版本。

務必保留：
- 標題「人類智慧不是單一商品」
- 中心「人類智慧」
- 六個能力節點與完整標籤：語言、感知、空間、身體、情感、創造力
- LLM 小圖示與標籤「語言能力很強，但不是全部智慧」
- 底部標語「智慧成本歸零，是錯誤問題」

### 5A. pm-workflow.png 16:9

依據文章第六節生成資訊圖，主題是「產品經理工作流前後對照」，台灣繁體中文，粉圓體，16:9。

畫面左右對比：
左側「過去：數月循環」流程：
PM → 設計師／工程師 → 原型 → 使用者回饋 → 整理需求。
標籤：「等待排程」、「跨部門協調」、「循環慢」。

右側「現在：AI 增幅快速循環」流程：
PM + AI → 快速原型 → 使用者模擬／回饋 → 專家深化。
標籤：「先做初版」、「快速驗證」、「專家做更難的事」。

中間放壓縮時間箭頭：「從數月 → 週末／數天」。

### 5B. pm-workflow-mobile.png 9:16

依據 5A 的原始 16:9 圖，重新繪製成 9:16 直式版本。

務必保留：
- 標題「產品經理工作流：AI 前後對照」
- 上半部「過去：數月循環」完整流程
- 中間箭頭「從數月 → 週末／數天」
- 下半部「現在：AI 增幅快速循環」完整流程
- 三個新流程標籤：「先做初版」、「快速驗證」、「專家做更難的事」

### 6A. barbell-workers.png 16:9

依據文章第七節生成資訊圖，主題是「兩種工作者：頂尖專家與高能動性通才」，台灣繁體中文，粉圓體，16:9。

畫面是一個槓鈴結構：
左端大圓「頂尖專家」：深技藝、頂尖品味、不可替代判斷。
右端大圓「高能動性通才」：快速學習、整合工具、推動事情發生。
中間細桿標籤：「中等單一技能承壓」。

在兩端上方都放共同標籤「都需要 agency」。底部補一句：「AI 讓一般產出變便宜，讓判斷與能動性更稀缺」。

### 6B. barbell-workers-mobile.png 9:16

依據 6A 的原始 16:9 圖，重新繪製成 9:16 直式版本。

務必保留：
- 標題「未來人才的雙峰結構」
- 上方大卡「頂尖專家」與三個標籤：深技藝、頂尖品味、不可替代判斷
- 中間細桿／警示「中等單一技能承壓」
- 下方大卡「高能動性通才」與三個標籤：快速學習、整合工具、推動事情發生
- 共同標籤「都需要 agency」

### 7A. spatial-agency.png 16:9

依據文章第九節與第十節生成資訊圖，主題是「空間智慧與 agency 路徑」，台灣繁體中文，粉圓體，16:9。

畫面分成左右兩區：
左區標題「空間智慧四要素」：四象限
1. 理解：看懂人、物、環境
2. 推理：路徑、距離、操作
3. 生成：2D／3D／4D 場景
4. 互動：摺衣服、移動、拿取

右區標題「agency 培養路徑」：垂直流程
安全感 → 嘗試風險 → 失敗學習 → 復原力 → 好奇心 → 獨立判斷。

中間用橋接箭頭標籤：「AI 不只語言，也要回到真實世界；人不只使用工具，也要承擔判斷」。

### 7B. spatial-agency-mobile.png 9:16

依據 7A 的原始 16:9 圖，重新繪製成 9:16 直式版本。

務必保留：
- 標題「空間智慧 × agency」
- 上半部四象限「空間智慧四要素」：理解、推理、生成、互動，含各自短說明
- 中間橋接標籤：「AI 回到真實世界，人承擔判斷」
- 下半部流程「agency 培養路徑」：安全感 → 嘗試風險 → 失敗學習 → 復原力 → 好奇心 → 獨立判斷

