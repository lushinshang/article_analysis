# 🎓 Microsoft Azure AI Fundamentals (AI-900) 繁體中文學習系統

本目錄收錄了 Microsoft Azure AI Fundamentals (AI-900) 認證考試的繁體中文精選模擬題庫（共計 475 題）、核心觀念重點整理、分析 298 題庫編製的關鍵速讀精華，以及兩套互動式備考心智圖播放器，並提供現代化、直覺且護眼的網頁入口介面，助您順利通過認證。

本系統已完全優化為標準靜態網頁架構，支援手機與桌面端 RWD 瀏覽，適合隨身閱讀並可直接部署至 GitHub Pages 上線使用。

另外也包含 AI-900 十輪模擬評量的復盤筆記：

- `pages/ai900_review_2026-06-28.html`：第一輪錯題復盤。
- `pages/ai900_review_2026-06-28_round2.html`：第二輪錯題復盤。
- `pages/ai900_review_2026-06-28_round3.html`：第三輪錯題復盤。
- `pages/ai900_review_2026-06-29_round4.html`：第四輪錯題復盤。
- `pages/ai900_review_2026-06-29_round5.html`：第五輪錯題復盤。
- `pages/ai900_review_2026-06-29_round6.html`：第六輪錯題復盤。
- `pages/ai900_review_2026-06-29_round7.html`：第七輪錯題復盤。
- `pages/ai900_review_2026-06-30_round8.html`：第八輪錯題復盤。
- `pages/ai900_review_2026-06-30_round9.html`：第九輪錯題復盤。
- `pages/ai900_review_2026-06-30_round10.html`：第十輪滿分復盤。
- `pages/ai900_review_2026-06-28_combined.html`：十輪綜合復盤總頁。

---

## 📂 目錄檔案結構

本學習系統主要由以下檔案與資料夾組成：

```
/
├── index.html                   # 核心入口網頁。Soft UI 卡片式導覽首頁，整合各單元捷徑。
├── README.md                    # 本說明文件。
├── css/
│   └── styles.css               # 全系統共用的核心樣式表，提供 Soft UI 護眼配色風格。
├── js/
│   └── script.js                # 題庫的核心互動邏輯（顯示答案、篩選大綱等）。
├── assets/
│   └── img/                     # 存放靜態圖片資源。
│       ├── mindmap-gpt/         # GPT 版備考心智圖 (01.png ~ 10.png)
│       └── mindmap-banana/      # Banana 版備考心智圖 (01.png ~ 10.png)
└── pages/                       # 存放所有核心學習子網頁。
    ├── ai900_quiz_machine.html  # 考前刷題機。整合 475 題隨機出題、自動判分與錯題收藏。
    ├── memory.html              # 關鍵速讀整理。高對比度易讀設計的 298 題精華重點與即時測驗。
    ├── mindmap_gpt.html         # 備考心智圖 (GPT版)。支援投影片播放與鍵盤控制的科技藍心智圖。
    ├── mindmap_banana.html      # 備考心智圖 (Banana版)。香蕉黃暖色調心智圖播放器。
    ├── AI-900_part1_268題.html  # 精選考題 (I)。第一部分 268 題基礎觀念檢定。
    ├── AI-900_part2_119題.html  # 精選考題 (II)。第二部分 119 題，著重電腦視覺與 NLP。
    ├── AI-900_part3_88題.html   # 精選考題 (III)。第三部分 88 題考前衝刺。
    ├── AI-900_part4.html        # 重點整理。歸納負責任 AI、機器學習類型與指標。
    ├── ai900_review_2026-06-28.html           # 第一輪錯題復盤。
    ├── ai900_review_2026-06-28_round2.html     # 第二輪錯題復盤。
    ├── ai900_review_2026-06-28_round3.html     # 第三輪錯題復盤。
    ├── ai900_review_2026-06-29_round4.html     # 第四輪錯題復盤。
    ├── ai900_review_2026-06-29_round5.html     # 第五輪錯題復盤。
    ├── ai900_review_2026-06-29_round6.html     # 第六輪錯題復盤。
    ├── ai900_review_2026-06-29_round7.html     # 第七輪錯題復盤。
    ├── ai900_review_2026-06-30_round8.html     # 第八輪錯題復盤。
    ├── ai900_review_2026-06-30_round9.html     # 第九輪錯題復盤。
    ├── ai900_review_2026-06-30_round10.html    # 第十輪滿分復盤。
    ├── ai900_review_2026-06-28_combined.html   # 十輪綜合復盤總頁。
    └── articles/                # 備考筆記系列文章。
        └── 《AI-900》...         # 13 篇深度觀念解析與心得分享 HTML。
```

---

## 🚀 使用說明

1. **啟動入口**：在瀏覽器中直接開啟根目錄的 **`index.html`**。
2. **切換單元**：在首頁主選單中點擊任一卡片（如考前刷題機、心智圖、精選考題），即可跳轉至對應的子網頁（路徑均位於 `pages/`）。
3. **心智圖操作**：
   - 點擊「上一張」/「下一張」按鈕，或使用鍵盤 **左 / 右方向鍵** 進行切換。
   - 支援全螢幕瀏覽模式與下方縮圖快速跳轉。
4. **返回首頁**：在任何子網頁的最上方或明顯處，皆有提供 `🏠 回到首頁主選單` 連結，可快速返回。
5. **復盤筆記**：直接開啟 `pages/ai900_review_2026-06-28_combined.html` 可查看十輪綜合復盤；若要看單輪明細，依序開啟 `round2`、`round3`、`pages/ai900_review_2026-06-29_round4.html`、`pages/ai900_review_2026-06-29_round5.html`、`pages/ai900_review_2026-06-29_round6.html`、`pages/ai900_review_2026-06-29_round7.html`、`pages/ai900_review_2026-06-30_round8.html`、`pages/ai900_review_2026-06-30_round9.html` 或 `pages/ai900_review_2026-06-30_round10.html`。
6. **部署至 GitHub Pages**：
   - 本專案已完全採用純前端靜態技術，無須任何後端與資料庫。
   - 直接將本專案目錄推送到您的 GitHub 儲存庫，並在 Settings -> Pages 中啟用，即可隨時隨地用手機進行刷題與複習。

---

## ✨ 系統功能特色

* **行動端最佳化 (RWD)**：全站網頁均支援手機、平板與桌面端瀏覽，排版自動適應。
* **舒適護眼配色**：精選低飽和度與高對比色調，減少長時間刷題時的眼睛疲勞。
* **獨立考前刷題機**：提供 475 題整合隨機練習、單選/複選自動判分、錯題複習、收藏題、未答題與本機進度保存。
* **互動式心智圖**：設計了兩套（科技藍 GPT 版、溫暖黃 Banana 版）互動式心智圖幻燈片，可快速梳理 AI-900 五大領域的連貫性。
* **命題大綱過濾器**：可針對特定的 AI 領域大綱（例如：電腦視覺、機器學習原則、NLP 工作負載等）進行題目篩選。
* **100% 繁體中文（台灣用語）**：題目與解析皆為高質量的中文翻譯，並保留對應之英文專有名詞，避免翻譯腔造成理解障礙。
