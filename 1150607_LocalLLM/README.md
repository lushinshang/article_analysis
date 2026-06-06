# 地端 LLM 檢索機制的發展與可能性

研究報告製作紀錄 · 2026-06-06 ~ 2026-06-07

---

## 專案概覽

本目錄為研究報告的完整輸出，包含 HTML 正式版、AI 生成資訊圖表及 QA 截圖。

```
地端LLM檢索/
├── index.html                  # 完整獨立 HTML（52KB，無需 build）
├── images/
│   ├── llm_wiki_comparison.png     # §4 LLM Wiki vs 傳統 RAG 對比（AI 生成，16:9）
│   ├── harness_leverage.png        # §6 Harness 量化槓桿效應（AI 生成，16:9）
│   └── scale_decision_matrix.png   # §8 資料量規模決策矩陣（AI 生成，16:9）
├── qa_desktop.png              # Playwright QA 截圖（1280×800）
├── qa_mobile.png               # Playwright QA 截圖（390×844）
└── README.md                   # 本文件
```

原始 Markdown：`../地端LLM檢索機制的發展與可能性.md`（603 行）

---

## 研究動機與問題設定

起點是 Google Research 於 2026-06-05 發表的 Agentic RAG 論文。使用者提問：

> 「不靠 Gemini，靠地端 AI，是否可以做到 Agentic RAG？Karpathy 的 LLM Wiki 是不是一招？」

問題逐步擴展為：
1. 地端環境能否重現 Agentic RAG 的核心機制？
2. LLM Wiki 在地端檢索中扮演什麼角色？
3. Grep vs 向量的爭論，答案是什麼？
4. Gemma 4 12B 的 Agentic 特性是否適合地端 RAG？
5. 資料量規模對架構設計有何決定性影響？

---

## 核心來源（7 個）

| 來源 | 標題 | 日期 |
|------|------|------|
| Google Research | Unlocking dependable responses with Agentic RAG | 2026-06-05 |
| a16z | Why We Need Continual Learning | 2026-04-22 |
| 愛好 AI 工程 Blog | 向量已死? Grep 萬能? 你需要的是「策展」一組檢索工具 | 2026-06-03 |
| Andrej Karpathy | LLM Wiki Pattern（GitHub Gist） | 2026 |
| Google Developers | Bring agentic skills to the edge with Gemma 4 | 2026-06-03 |
| GitHub | lucasastorian/llmwiki（開源實作，⭐1.1k，Apache 2.0） | 2026 |
| GitHub | ai-boost/awesome-harness-engineering | 2026 |

---

## 執行流程

### Step 1：來源分析與框架建立

四個初始來源各自解決不同層次的問題：

- **Google Research**（中層）：多代理人架構 + Sufficient Context Agent
- **a16z**（巨觀）：持續學習光譜，RAG 的根本限制
- **aihao.tw**（微觀）：grep vs 向量的實測數據，混合檢索工程標準
- **Karpathy**（設計模式）：LLM Wiki 的知識預消化架構

三層合成框架：地端工具選擇（micro）→ 架構組合（middle）→ 學習典範（macro）。

### Step 2：研究 MD 撰寫

使用 `deep-guide` skill，產出 `地端LLM檢索機制的發展與可能性.md`（603 行，10 個章節）。

主要章節：
1. 前言：epistemic awareness 的重要性
2. 標準 RAG 的結構性死局
3. Agentic RAG：五代理人的認知分層
4. LLM Wiki：知識預消化革命
5. Grep、向量、還是混合？
6. Harness 設計：決定性能的真正變數
7. Gemma 4 12B：地端 Agent 的新拼圖
8. 資料量對架構規劃的決定性影響
9. 持續學習：檢索的終極邊界
10. 地端 LLM 檢索的未來路線圖

### Step 3：Opus 4.8 事實查核

子 Agent（claude-opus-4-8）進行嚴謹度審查，發現並修正以下問題：

| 原文錯誤 | 修正 |
|----------|------|
| "LLM Aggregator" | → "Synthesis Agent"（來源原文用語） |
| "第六個隱含角色" | → "來源中明確命名的角色" |
| 雙峰分布 50%/30%/20%（假精確數字） | → 改為定性描述，標注「示意，非原文數據」 |
| "16GB RAM" 作為 12B 硬性規格 | → 改為家族行銷說法，指向 E2B <1.5GB 為驗證數字 |

### Step 4：Opus 4.8 可行性審查

發現並修正以下可行性問題：

| 問題 | 修正 |
|------|------|
| 「延遲增加不超過 3%」 | → 加 ⚠️：此為雲端 TPU 數字，地端現實 3–10× |
| Ollama 多模型並存 | → 加 ⚠️：load/unload 延遲問題，建議 vLLM/TGI |
| LLM Wiki「維護成本幾乎為零」 | → 加維護成本表（算力、回歸風險、Lint 全庫掃描、漂移）|
| 迴圈防呆未提及 | → 新增五項 loop guard 要求 |
| 規模矩陣以文件份數為主維度 | → 加 ⚠️：主維度應為 chunk 數；跨層升級警告 |
| 12B vs 70B 能力矛盾 | → 加 12B 能力邊界說明（4–5+ 步計畫失敗模式） |

### Step 5：GitHub 探索

搜尋補充來源，Opus 4.8 審查後選出最高價值兩個：
- **A（8.5/10）**：lucasastorian/llmwiki — LLM Wiki 開源實作（FTS5 + MCP）
- **C（8.0/10）**：ai-boost/awesome-harness-engineering — Harness 量化彙整

整合到 §4 與 §6，補充具體量化數據與開源落地參照。

### Step 6：MD → HTML 轉換

使用 `md_to_html` skill，步驟：

1. **AI 圖片生成**（Codex CLI，`codex_imagegen.py`）：
   - `images/llm_wiki_comparison.png`：傳統 RAG vs LLM Wiki 三層架構對比
   - `images/harness_leverage.png`：Harness 量化槓桿效應（84%、12–23%、67%、Azure SRE）
   - `images/scale_decision_matrix.png`：四層規模決策矩陣

2. **HTML 建構**：深綠漸層 Hero、sticky nav、10 章節錨點、warning block、stat-grid、action-cards

3. **Playwright QA**：桌機（1280×800）與手機（390×844）截圖驗證

### Step 7：UI Review 與 Bug 修復

Playwright 逐段截圖審查，發現並修復：

**嚴重 Bug**：`nav { position: sticky }` CSS 選到 `<nav class="toc">` → TOC 雙層黏頂
- 修復：改為 `nav[aria-label="章節導覽"] { position: sticky }`

**其他調整**：nav「資料量」標籤縮短為「規模」，避免 1280px 截斷

### Step 8：Lightbox 功能

三張 AI 生成圖片（圖小字多）加入點擊放大 Lightbox：
- 只對 `.infographic img` 作用，外部圖片不影響
- `zoom-in` cursor 提示
- 最大 `min(1400px, 96vw)`，`object-fit: contain`
- 三種關閉：✕ 按鈕、點背景、Esc 鍵
- 開啟時鎖定 body scroll

---

## 關鍵技術決策

### 為什麼不用 CSS framework？
HTML 需要完全獨立（無 build step），全部 CSS inline 在 `<style>`，無外部依賴。

### 外部圖片為何保留原 URL 而非下載？
外部圖片（Google Research、a16z CDN）有版權疑慮，以 `<img>` 引用原址，在正式部署環境（有正確 origin）應正常顯示。localhost 可能因 referer 政策顯示 broken。

### Lightbox 為何只套用 infographic？
外部圖片無法控制原始尺寸，放大意義不大；AI 生成圖「圖小字多」才是需要放大的使用情境。

---

## 最終審查結果

| 項目 | 結果 |
|------|------|
| 事實嚴謹度（Opus 4.8） | 8 / 10 |
| 可行性評分（Opus 4.8） | 6 / 10（修正後） |
| 整合嚴謹度 | **8.7 / 10** |
| HTML 語法驗證 | ✅ python3 -m html.parser 通過 |
| Desktop QA | ✅ |
| Mobile QA | ✅ |
| Lightbox 功能測試 | ✅ 開啟 + Esc 關閉均正常 |
