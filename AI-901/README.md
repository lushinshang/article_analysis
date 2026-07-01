# AI-901 Microsoft Azure AI Fundamentals 互動備考教材

> 針對 **AI-901**（2026/04/15 更新版考綱）設計的全中英雙語互動備考系統。
> 內含 300 道模擬題（含答案解析）與 6 個深度學習模組。

---

## 專案概覽

| 項目 | 內容 |
|------|------|
| 考試 | Microsoft AI-901: Azure AI Fundamentals |
| 及格分數 | 700 / 1000 |
| 主要入口 | `index.html`（單一 HTML 離線可用）|
| 題目數量 | 300 題（雙語 + 解析）|
| 學習模組 | 6 個官方路徑模組 + 考試概覽 |

---

## 功能特色

### 📚 教材模式
- 考試概覽頁：兩大領域比重、技能清單、AI-900 vs AI-901 差異對照
- 6 個學習模組（對應官方 learning path）：
  - 模組 1：AI 工作負載與負責任 AI
  - 模組 2：機器學習基礎與 Foundry 架構
  - 模組 3：電腦視覺與影像生成
  - 模組 4：自然語言與語音解決方案
  - 模組 5：生成式 AI 與 AI 代理人
  - 模組 6：文件智慧與資訊擷取專題
- Mermaid 架構圖（支援放大 modal）
- 列印 / 匯出 PDF（按鈕一鍵啟動瀏覽器列印）

### 🎯 模擬題庫模式
- 300 道雙語（中英）模擬題
- 7 大分類篩選：負責任 AI、模型組件、AI 工作負載、生成式 AI 與代理、文字與語音、電腦視覺與影像、資訊擷取
- 題型涵蓋：單選題、多選題、Yes/No 選項題、下拉選單題、拖拉配對題、程式碼補空題
- 即時答案回饋 + 詳細中文解析
- 英中並排切換
- 題目分頁（上一題 / 下一題）
- 重新開始功能
- 當前測驗進度顯示（已答題數、答對率、進度條）
- **下載 CSV** 功能（含 BOM，Excel 直開中文正常）

### 🔗 官方資源整合（側邊欄快捷連結）
- Exam AI-901 考試說明頁
- 考試技能大綱 PDF 下載
- 學習路徑：AI 基礎概念
- 學習路徑：AI 應用與代理人
- 官方練習評量（即將上線）

### 🎨 介面設計
- 護眼淺色主題（冷調米白 `#f4f7fb` + 深石板文字 `#0f172a`）
- 程式碼區塊維持深色（視覺「島嶼對比」）
- 完整 RWD：桌面雙欄佈局 / 手機抽屜式側邊欄
- 觸控目標 ≥ 44px（WCAG 2.5.5）
- iOS Safari 修正：`font-size: 16px` 防 select 縮放、`100dvh` 防 viewport 溢出
- `prefers-reduced-motion` 動畫豁免
- 超小螢幕（≤360px）專屬斷點

---

## 檔案結構

```
AI-901/
├── index.html              # 主程式（教材 + 題庫 + 互動邏輯）
├── ai901_classic_guide.html # 舊版簡易教材（備存，不上傳）
└── README.md               # 本說明文件
```

---

## 技術棧

| 項目 | 內容 |
|------|------|
| 前端 | 純 HTML5 + CSS3 + Vanilla JS（零依賴）|
| 字體 | Google Fonts：Inter、Noto Sans TC、JetBrains Mono |
| 圖表 | Mermaid.js v10（CDN）|
| 題庫儲存 | JavaScript 陣列（嵌入 HTML，離線可用）|
| CSV 匯出 | Blob + `createObjectURL`（含 UTF-8 BOM）|
| 列印 PDF | `@media print` + `window.print()` |
| RWD | CSS Grid + `clamp()` + `dvh`/`svh` |

---

## 如何使用

1. 下載 `index.html` 到本機
2. 用任何瀏覽器直接開啟（無需伺服器）
3. 教材模式：點選左側模組導覽閱讀學習內容
4. 題庫模式：切換至「模擬題庫」，選擇分類開始練習
5. 匯出：教材可列印 PDF，題庫可下載 CSV

---

## 考試兩大領域

```
Domain 1: 識別 AI 概念與能力      40–45%
  ├─ 負責任 AI 六大原則
  ├─ AI 模型組件與設定
  └─ AI 工作負載辨識

Domain 2: 使用 Microsoft Foundry 實作  55–60%
  ├─ 生成式 AI 應用與代理人
  ├─ 文字分析與語音解決方案
  ├─ 電腦視覺與影像生成
  └─ Content Understanding 資訊擷取
```

---

## 官方資源

| 資源 | 連結 |
|------|------|
| 考試說明頁 | https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-901/ |
| 考試技能大綱 | https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901 |
| 學習路徑 AI 概念 | https://learn.microsoft.com/en-us/training/paths/ai-concepts/ |
| 學習路徑 AI 應用與代理 | https://learn.microsoft.com/en-us/training/paths/get-started-ai-apps-agents/ |
| 認證總覽 | https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/ |

---

## 資料來源聲明

題庫與教材內容依據以下官方文件編製，僅供備考學習使用：

- [Exam AI-901 Study Guide — Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901)（2026-04-15 更新版）
- [Microsoft Azure AI Fundamentals 官方學習路徑](https://learn.microsoft.com/en-us/training/paths/ai-concepts/)
- Microsoft Azure 官方文件：Foundry Portal、Azure Speech、Azure Content Understanding、Azure AI Vision

> ⚠️ 本材料非 Microsoft 官方出版物，所有商標歸 Microsoft Corporation 所有。

---

## 題庫生成進度（建置日誌）

### 整體規劃

目標：300 道雙語模擬題，7 大分類，ID 1-300。

| 分類 | category key | 目標題數 | ID 範圍 |
|------|-------------|---------|--------|
| 負責任 AI | responsible-ai | 42 | 1-7（既有）+ 51-85 |
| AI 模型組件 | model-components | 48 | 8-15（既有）+ 86-125 |
| AI 工作負載 | workloads | 18 | 16-17（既有）+ 126-141 |
| 生成式 AI 與代理人 | gen-ai-foundry | 55 | 18-26（既有）+ 142-187 |
| 文字與語音 | text-speech-foundry | 42 | 27-33（既有）+ 188-222 |
| 電腦視覺與影像生成 | vision-foundry | 42 | 34-41（既有）+ 223-256 |
| 資訊擷取 | info-extraction-foundry | 53 | 42-50（既有）+ 257-300 |

> 括號內為 index.html 嵌入的既有 50 題（ID 1-50），各分類實際數字以 index.html 為準。

### 完成狀態 ✅

| 分類 | ID 範圍 | 題數 | 狀態 |
|------|--------|------|------|
| 既有題庫（7 分類混合）| 1-50 | 50 | ✅ |
| responsible-ai | 51-85 | 35 | ✅ |
| model-components | 86-125 | 40 | ✅ |
| workloads | 126-141 | 16 | ✅ |
| gen-ai-foundry | 142-187 | 46 | ✅ |
| text-speech-foundry | 188-222 | 35 | ✅ |
| vision-foundry | 223-256 | 34 | ✅ |
| info-extraction-foundry | 257-300 | 44 | ✅ |
| **合計** | **1-300** | **300** | ✅ **已嵌入 index.html** |

### 最終分類分布

| 分類 | 題數 |
|------|------|
| gen-ai-foundry | 55 |
| info-extraction-foundry | 53 |
| model-components | 48 |
| responsible-ai | 42 |
| text-speech-foundry | 42 |
| vision-foundry | 42 |
| workloads | 18 |
| **Total** | **300** |
