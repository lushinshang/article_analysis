# 地端 LLM 檢索機制的發展與可能性

> **研究日期**：2026 年 6 月 6 日  
> **關鍵字**：Agentic RAG、LLM Wiki、Continual Learning、Harness 設計、Gemma 4、地端 AI

---

## 核心來源

| 來源 | 標題 | 日期 |
|------|------|------|
| Google Research | [Unlocking dependable responses with Gemini Enterprise Agent Platform's Agentic RAG](https://research.google/blog/unlocking-dependable-responses-with-gemini-enterprise-agent-platforms-agentic-rag/) | 2026-06-05 |
| a16z | [Why We Need Continual Learning](https://a16z.com/why-we-need-continual-learning/) | 2026-04-22 |
| 愛好 AI 工程 Blog | [向量已死? Grep 萬能? 不，你需要的是「策展」一組檢索工具](https://blog.aihao.tw/2026/06/03/is-grep-all-you-need/) | 2026-06-03 |
| Andrej Karpathy | [LLM Wiki Pattern (GitHub Gist)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | 2026 |
| Google Developers | [Bring state-of-the-art agentic skills to the edge with Gemma 4](https://developers.googleblog.com/bring-state-of-the-art-agentic-skills-to-the-edge-with-gemma-4/) | 2026-06-03 |

---

## 目錄

1. [前言：當系統開始懂得說「我還不知道」](#1-前言當系統開始懂得說我還不知道)
2. [標準 RAG 的結構性死局](#2-標準-rag-的結構性死局)
3. [Agentic RAG：五代理人的認知分層](#3-agentic-rag五代理人的認知分層)
4. [LLM Wiki：Karpathy 的知識預消化革命](#4-llm-wikikarpathy-的知識預消化革命)
5. [Grep、向量、還是混合？地端檢索工具的真相](#5-grep向量還是混合地端檢索工具的真相)
6. [Harness 設計：決定性能的真正變數](#6-harness-設計決定性能的真正變數)
7. [Gemma 4 12B：地端 Agent 的新拼圖](#7-gemma-4-12b地端-agent-的新拼圖)
8. [資料量對架構規劃的決定性影響](#8-資料量對架構規劃的決定性影響)
9. [持續學習：檢索的終極邊界](#9-持續學習檢索的終極邊界)
10. [地端 LLM 檢索的未來路線圖](#10-地端-llm-檢索的未來路線圖)

---

## 1. 前言：當系統開始懂得說「我還不知道」

AI 系統最危險的缺陷，不是找不到答案，而是找到了一個自信滿滿的錯答案。

問企業知識庫：「Project X 用的伺服器規格是什麼？」  
系統找到一份 Project X 的文件，裡面只寫著「使用 Server ID: SRV-204」。  
然後它把這句話包裝成完整答案回傳給你。

技術上，它「找到了」。業務上，它給了你一張沒有地址的地圖。

這個場景正是 2026 年 AI 檢索機制演化的驅動力。從 Google Research 的 Agentic RAG、Karpathy 的 LLM Wiki、到 a16z 對持續學習的呼籲，各方正在不同層次解決同一個問題：**讓系統知道自己不知道什麼，並且知道如何去補齊它。**

本文整合五個核心來源，從微觀的檢索工具選擇，到巨觀的學習典範轉移，為台灣 AI 從業者提供一份實戰導向的地端 LLM 檢索機制全景分析。

---

## 2. 標準 RAG 的結構性死局

![Agentic RAG Cover](https://storage.googleapis.com/gweb-research2023-media/original_images/AgenticRAG_Cover.png)

標準 RAG（Retrieval-Augmented Generation）的邏輯看似直觀：

```
使用者問題 → 向量搜尋 → 取回相關文件片段 → LLM 合成答案
```

這個流程在「問題答案剛好在同一份文件」時表現優異。但企業知識庫的現實從來不是這樣長的。

### 三個不可迴避的結構性問題

**問題一：多跳推理（Multi-hop Reasoning）**  
現實中的業務問題往往需要跨越多個文件、多個資料庫才能拼湊出完整答案。「Project X 的伺服器規格」可能需要：文件 A（找到 server ID）→ 文件 B（ID 對應到型號）→ 規格資料庫（型號對應規格）。標準 RAG 的單步搜尋根本無法完成這個推理鏈。

**問題二：假完整性（False Completeness）**  
當搜尋結果不足，系統不會說「我不確定」——它會用手邊殘缺的資訊，生成一個語氣流暢但實際有缺口的答案。這種「自信的不完整」比明顯的錯誤更難被發現。

**問題三：知識孤島（Knowledge Silos）**  
企業資料分散在 HR 系統、財務記錄、技術文檔、客服歷史、CRM 等不同系統中。單一向量資料庫無法涵蓋全貌，但同時查詢多個資料庫又面臨「選哪個庫」的路由問題。

這三個問題共同指向一個根本缺陷：**標準 RAG 假設一次搜尋就能取得足夠的上下文——這個假設在企業環境中幾乎永遠是假的。**

---

## 3. Agentic RAG：五代理人的認知分層

![Agentic RAG 架構對比](https://storage.googleapis.com/gweb-research2023-media/original_images/AgenticRAG3_Comparison.png)

Google Research 在 2026 年 6 月發表的研究，提出了超越標準 RAG 的多代理人架構。核心洞見是：**把「理解問題、搜尋資料、合成答案」這三件事拆解成五個認知層次，分別由專門的代理人負責。**

### 五大代理人的分工邏輯

| 代理人 | 認知層次 | 核心職責 |
|--------|----------|----------|
| **Orchestrator** | 意圖理解 | 評估請求性質，決定委派策略 |
| **Planner Agent** | 資訊地圖 | 規劃「需要哪些資料、從哪裡取」 |
| **Query Rewriter** | 搜尋語言翻譯 | 將自然語言轉換成多個精準查詢 |
| **Search Fanout Agent** | 並行執行 | 將精煉查詢分發至多個資料來源 |
| **Synthesis Agent** | 語意整合 | 跨來源合成最終答案 |

這五層分離有一個關鍵好處：每一層都可以獨立優化，失敗也可以獨立偵測，不再是難以追蹤的黑盒。

### 核心創新：Sufficient Context Agent

讓整個框架質變的，是來源中明確命名的 **Sufficient Context Agent（充分上下文代理）**——它與上述五個代理人並列，專責品質驗證。

它做的事情說起來簡單：在把資料交給最終合成前，先問一個問題——「這些資料夠回答原始問題嗎？」

但要讓機器真正理解「夠」，需要三層判斷：

1. **片段層**：取回的文字本身是否包含有效資訊，還是只是關鍵字命中但語意無關？
2. **草稿層**：初步生成的答案是否有明確的邏輯缺口，還是看起來完整但語焉不詳？
3. **缺口層**：如果不夠，缺的是什麼？要用什麼查詢去補？

這個設計賦予 AI 系統真正的 **epistemic awareness（知識邊界意識）**——知道自己不知道什麼，並且主動採取行動補齊。

### 效能驗證

Google 在 FramesQA 基準測試（824 個多跳問題，來自 2,676 份 PDF）中的結果：

- **跨語料庫選庫準確率**：90.1%（在 4 個資料庫中選出正確來源）
- **事實性準確率提升**：相比標準 RAG 提升最多 **34%**
- **延遲增加**：跨語料庫與單一語料庫相差 **不超過 3%**（⚠️ 此數字為 Google 雲端 TPU 基礎設施上的量測結果，比較基準是「單一語料庫 vs 跨語料庫路由」，並非標準 RAG vs Agentic RAG 的總延遲差。地端環境受限於 Ollama 序列化、消費級硬體 decode 速率（7–31 tokens/s）與多輪迴圈放大效應，Agentic RAG 相對標準單次 RAG 的延遲增幅，現實中可能是 **3–10 倍**，不可直接移植此 3% 數字。）

34% 的準確率提升在雲端的 ROI 是顯著的——但地端採用者必須先以自身硬體實測延遲，再評估商業可行性。

> **重要性**：Agentic RAG 框架的設計讓每一步都有可追溯的中間狀態，答案從「你要信任它」變成「你可以驗證它」。在金融、法務、醫療等高風險行業，「可驗證性」本身就是產品核心競爭力。

---

## 4. LLM Wiki：Karpathy 的知識預消化革命

Andrej Karpathy 在 GitHub Gist 提出的 LLM Wiki 模式，解決了一個前面三個問題都沒正面處理的根本缺陷：**原始文件本身就是噪音。**

### 核心翻轉

```
傳統 RAG：
原始文件 ──[每次查詢時取回]──→ LLM 重新理解 → 答案
成本在 query-time，且每次都重新從零開始

LLM Wiki：
原始文件 ──[一次性 ingest]──→ 結構化 Wiki ──[查詢時讀 Wiki]──→ LLM → 答案
成本在 ingest-time，查詢時只需讀已消化的知識
```

### 三層架構

**Layer 1 — Raw Sources（不可變的原始來源）**  
你策展的原始文件：論文、會議記錄、產品文件、技術規格。人類負責策展，LLM 不修改原始來源。

**Layer 2 — The Wiki（LLM 維護的知識庫）**  
由互相連結的 Markdown 頁面構成的知識圖譜。每次有新原始文件進來，LLM 不只是「歸檔」，而是將新知識**融入**現有的 10–15 個相關頁面。知識在這裡累積、整合、交叉引用。

**Layer 3 — The Schema（行為協議）**  
一份類似 CLAUDE.md 的配置文件，定義 LLM 如何維護 wiki——什麼格式、什麼交叉引用規則、什麼品質標準。

### 三個核心操作

| 操作 | 觸發時機 | LLM 做的事 |
|------|----------|------------|
| **Ingest** | 新文件加入 | 理解內容，融入相關 Wiki 頁面，建立交叉引用 |
| **Query** | 使用者提問 | 讀取相關 Wiki 頁面合成答案；好答案本身也成為新頁面 |
| **Lint** | 定期排程 | 偵測矛盾、過時內容、孤立頁面、缺失交叉引用 |

### 與 a16z 壓縮論的呼應

a16z 指出，LLM 訓練的本質是把海量資料**壓縮**成模型參數。LLM Wiki 把同樣的壓縮邏輯搬到 inference time——wiki 是存在 Markdown 檔案裡的壓縮知識快取，不是模型權重，但服務相同的目的。

這讓 LLM Wiki 成為整個學習光譜上的重要中繼站：不需要修改模型權重，卻讓系統累積並整合知識，而不是每次查詢都重新從零理解。

### LLM Wiki 的真實維護成本

Karpathy 的 gist 宣稱「維護成本幾乎為零」，實際上指的是**人力成本**降低——人類只需策展原始來源，LLM 負責書目整理。但以下成本不能忽視：

| 成本類型 | 說明 |
|----------|------|
| **算力成本** | 每次 Ingest 需要 LLM 讀寫 10–15 個現有頁面，複雜度隨 wiki 成長而上升 |
| **回歸風險** | 新文件觸發 LLM 改寫舊頁面，可能悄悄破壞已正確的內容 |
| **Lint 全庫掃描** | 矛盾/過時偵測本質是全庫遍歷，成本非固定值 |
| **漂移與幻覺** | LLM 自維護的 wiki 缺乏 ground truth，需要定期人工抽查 + git 版控追蹤變更 |

務實建議：把維護成本標定為「**低但非零**」，並建立 git 版控 + 定期 diff review 的紀律，讓 wiki 的演化可追溯。

### 現實世界實作參照

理論設計已有開源落地：**[lucasastorian/llmwiki](https://github.com/lucasastorian/llmwiki)**（⭐ 1.1k，Apache 2.0）是目前最具代表性的 Karpathy 模式實作，幾個設計選擇直接印證本文論點：

- **儲存層採 SQLite FTS5**（關鍵字全文搜尋），而非向量 DB——與本文 §5「結構化 Markdown 最適合 BM25/grep」的論點一致
- **介面為 MCP server**，支援 Claude、Cursor、Cline 等多種客戶端，不鎖定單一 AI
- **Filesystem 是 source of truth**，SQLite 是可重建的衍生 index——強化了 git 版控可追溯性

已知限制：一個 workspace 對應一個 MCP server（多專案需多配置）；本地模式無語意搜尋（需混合架構補足）。這與本文 §5 推薦「BM25 + 向量混合」的結論形成互補，而非衝突。

### 為地端部署量身設計

LLM Wiki 的輸出是**結構化 Markdown**——這正是最適合 grep 和 BM25 搜尋的格式。這不是巧合，而是讓「知識預消化」和「輕量地端檢索」天然互補的設計。

---

## 5. Grep、向量、還是混合？地端檢索工具的真相

PwC 論文《Is Grep All You Need?》引發的論戰，在 2026 年 6 月由愛好 AI 工程 Blog 做了清醒的梳理。

### Grep 的真正甜蜜點

研究發現，在特定場景下 grep 的準確率可以高達 **86.2%**，遠超向量檢索的 62.9%。但這個優勢有明確的適用條件：

✅ **grep 適合的場景**
- 對話記憶搜尋（字面關鍵字查詢）
- 程式碼識別字、變數名、函式名
- 產品編號、錯誤碼、精確查詢
- 結構清晰的純文字（例如：Karpathy 的 Wiki Markdown）

❌ **grep 不擅長的場景**
- PDF、圖片等非文字格式
- 同義詞替換、術語不一致
- 概念性、推理性的查詢
- 跨語言語意搜尋

### 雙峰查詢分布：設計 Harness 的關鍵輸入

來源描述實際企業查詢呈現雙峰特性：**約一半是對話式問句（語意查詢），另一半是精確查詢（如產品碼、錯誤碼），其中精確查詢往往佔超過 30% 的流量**。來源未提供精確百分比切分，以下比例為示意，非原文數據：

```
示意（非原文精確數據）：
對話式問句：~半數（語意查詢）
精確查詢：  ~30%+ （產品碼、錯誤碼、字面關鍵字）
混合型：    其餘部分
```

這個雙峰特性指向 Harness 的核心設計需求——應先做 query 分類器，自動將查詢路由到最適合的檢索路徑，而不是讓所有查詢都走同一條路。

### 混合檢索：現在的工程標準答案

| 層次 | 工具 | 適用 |
|------|------|------|
| 精確層 | BM25 / grep | 關鍵字、產品碼、程式碼 |
| 語意層 | 向量搜尋（local embedding）| 概念查詢、語意相似 |
| 融合層 | RRF（互補排名融合）| 整合兩種結果 |
| 重排層 | Cross-encoder reranker | 最終相關性排序 |
| 關係層 | GraphRAG（視需要）| 跨實體關係推理 |

> **2025–2026 趨勢數據**：導入混合檢索的意願從 2025 年初 10.3% 上升到年底 33.3%。「超長上下文淘汰檢索」的說法從 15.5% 跌至 3.5%——市場正在回歸務實。

### 語意版 Grep：新興工具

- **LlamaIndex semtools**：用 LlamaParse 處理 PDF + model2vec 本地語意搜尋
- **ColGrep（LightOn）**：整合 regex + 語意排序 + RRF，勝純 grep 約 70%
- **Jina jina-grep**：支援自然語言搜尋與管線語意重排

---

## 6. Harness 設計：決定性能的真正變數

愛好 AI 工程 Blog 引用 Elastic 的 Leonie Monigatti 的觀察：

> **「上下文工程大概有八成，其實就是代理式搜尋。」**

這句話揭示了一個被大多數開發者忽略的真相：**Harness（代理框架）的設計，對系統性能的影響遠超過選擇哪種檢索演算法。**

### 量化證據：Harness 的槓桿效應

以下數據來自 [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) 彙整的已發布 benchmark 與案例研究。⚠️ 各項數字的原始量測條件各異，僅作為量級參考，不宜跨情境直接套用。

| 工程決策 | 量化效益 | 備註 |
|----------|----------|------|
| Server-side context compaction | token 消耗下降 **84%** | web-search evals |
| Domain-specific context pruning | 額外節省 **31%** token | coding agent 情境 |
| Task topology 選擇（並行/序列/階層） | 性能差異 **12–23%** | **與模型選擇無關** |
| Router vs subagents 架構 | token 消耗差距 **67%** | cross-domain 情境 |
| Pre-action authorization（事前授權） | 攔截高風險行動 **100%** vs 寬鬆策略 **26%** | 安全測試 |

> ⚠️ **Azure SRE Agent 案例**：Harness 重新設計後，事件平均修復時間從 40.5 小時降至 3 分鐘。此數字為廠商公布的 best-case 對比，現實部署效益因情境差異顯著；但其方向明確：**這是 Harness 重設計的成果，沒有更換底層模型**。直接印證本文「Harness 投資優先於模型投資」的核心論點。

### 什麼是 Harness？

Harness 是 Agent 的執行框架，定義了：
- 代理人如何協作（任務分派、結果傳遞）
- 搜尋何時停止（終止條件）
- 失敗如何處理（重試、降級）
- 結果如何整合（融合、排序、驗證）

### 雙層迴圈設計

優秀的 Harness 設計應包含兩層迴圈（Doug Turnbull 的觀點）：

```
外層迴圈（品質驗證）
└── 內層迴圈（查詢迭代）
    ├── 發出查詢
    ├── 取回結果
    ├── 評估相關性
    └── 若不足 → 精煉查詢 → 重試
└── 若結果達標 → 合成最終答案
└── 若未達標 → 調整策略 → 重新進入內層迴圈
```

> ⚠️ **工程落地的隱藏複雜度**：迴圈防呆（loop guard）的開發量往往超過迴圈主邏輯本身。必須明確實作：
> - **max-iteration 上限**：防止無限迴圈（建議 3–5 次）
> - **cost budget**：限制單次查詢的 LLM 呼叫總量
> - **查詢去重**：避免相同查詢被反覆送出
> - **震盪偵測**：偵測 A→B→A 的循環模式並強制跳出
> - **退化偵測**：精煉後的查詢若比原始更差，應回退而非繼續細化

### Sufficient Context 的終止條件設計

Agentic RAG 框架的迴圈終止條件是**語意完整度**，而不是固定的搜尋次數上限。這個設計讓系統在簡單問題上快速收斂，在複雜問題上深度挖掘——但地端實作時，需要特別注意：

**Sufficient Context Agent 的地端實作建議：**

```python
# 用小型 judge 模型（不需要大模型）評估完整性
# 輸入：原始問題 + 已取回片段 + 初步草稿
# 輸出：{ "sufficient": bool, "missing": ["缺少什麼"], "refine_query": "精煉查詢" }
```

建議使用獨立的微調小模型（如 Llama 3.1 8B instruct）專門負責這個判斷步驟，而不是使用主模型——降低延遲，也降低大模型在 meta-reasoning 上的不穩定性。

### 地端最小可行 Harness 技術棧

```
模型服務層：【開發驗證】Ollama（易用，但並發弱）
            【上量生產】vLLM / llama.cpp server / TGI（真正的並發支援）
            模型選擇：Llama 3.3 70B（主推理）+ Llama 3.1 8B（Sufficient Context judge）
向量資料庫：Qdrant（self-host）或 ChromaDB（本地輕量）
Harness 框架：LlamaIndex（有內建 Agentic RAG 模板）
               LangGraph（更靈活的狀態機，適合複雜流程）
知識層：Karpathy LLM Wiki（Markdown + ripgrep）
```

> ⚠️ **Ollama 多模型共存警告**：Agentic 流程同時需要主模型 + judge 模型時，Ollama 預設會在模型間 load/unload，每次切換可能增加數秒延遲。正式部署前需壓測並發情境，或改用支援多模型常駐的 serving 引擎。

> ⚠️ **Sufficient Context Agent 的語意可靠性**：constrained decoding 只保證輸出語法合法（有效 JSON），**不保證判斷語意正確**——小模型可能吐出語法完美但判斷錯誤的 `"sufficient": true`。建議為 judge 模型建立獨立的評估集（golden set），量測 false-sufficient rate，並設定可接受的上限門檻後再上線。

---

## 7. Gemma 4 12B：地端 Agent 的新拼圖

![Gemma 4 Banner](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/gemma4_banner_2.original.png)

2026 年 6 月 3 日，Google 發布 Gemma 4 12B，這是第一款明確以**地端 Agentic 工作流**為設計核心的開源模型。

### 核心規格

| 特性 | 規格 |
|------|------|
| 上下文視窗 | 128K tokens |
| 語言支援 | 140+ 種語言 |
| E2B 精簡版記憶體 | < 1.5GB |
| 精簡版推薦硬體 | 16GB RAM 筆電（來源以 Gemma 4 家族為整體宣傳，非 12B 單獨規格）|
| 權重量化 | 2-bit / 4-bit 支援 |

**地端硬體效能**：
- Raspberry Pi 5（CPU）：133 prefill / 7.6 decode tokens/s
- 高通 Dragonwing IQ8（NPU）：3,700 prefill / 31 decode tokens/s

### Agent 特性解析

Gemma 4 12B 的 Agent 設計有三個對 Agentic RAG 特別有意義的特性：

**特性一：結構化輸出（Constrained Decoding）**  
受約束的解碼確保工具調用結果格式可預測。這對 Agentic RAG 至關重要——Orchestrator 和 Sufficient Context Agent 的輸出必須是可解析的 JSON，而不是自由格式文字。Gemma 4 的這個特性讓 Harness 的整合成本大幅降低。

**特性二：Gemma Skills Repository（官方技能庫）**  
Google 提供一個可重用技能的官方庫，專門為 Agentic 工作流設計。使用者可以直接調用預建的技能（如維基百科查詢、工具調用模板），這些技能與 LLM Wiki 的 Ingest / Query / Lint 操作天然對應。

**特性三：多步驟規劃能力**  
Gemma 4 明確支援 multi-step planning 和 autonomous action，這意味著：
- Planner Agent 的角色可以由單一 Gemma 4 模型承擔
- 不需要強行分離成多個不同模型的角色

### Gemma 4 12B 對地端 Agentic RAG 的意義

傳統地端 Agentic RAG 的困境：需要夠大的模型才能穩定地執行 Orchestrator / Planner 角色，但大模型（70B）在消費級硬體上速度不夠快。

Gemma 4 12B 改變了這個等式：

```
之前：需要 70B 模型才能穩定做 multi-step planning
之後：12B 的 Gemma 4 明確設計支援 Agentic 工作流

實際意義：
- Google 以「筆電可執行」作為整體定位宣傳（16GB RAM 為家族級推薦，非 12B 單獨驗證規格）
- 具體記憶體需求依量化等級而異（E2B 精簡版 < 1.5GB；完整精度需更多）
- 不再需要雲端 GPU 資源
- 成本大幅下降，隱私完全本地
```

> ⚠️ **12B 的能力邊界**：Gemma 4 12B 的 Agentic 設計在簡單 2–3 跳查詢上有意義，但在以下情境容易失敗：
> - **超過 4–5 步的長計畫**：容易丟失狀態、重複已完成步驟
> - **空結果或矛盾資料的錯誤恢復**：傾向「假裝沒事繼續」而非重新規劃
> - **跨工具參數傳遞**：多資料源混查時準確性顯著下降
>
> 複雜企業查詢建議以 70B 模型擔任 Orchestrator / Planner，12B 作為輔助角色（如輕量 judge 或單一工具呼叫）。文章第 §8 節的大型規模矩陣也明確建議「大型需要 70B 主模型」，實務上兩者角色分工優於單用 12B。

**與 Sufficient Context Agent 的搭配**：Gemma 4 的結構化輸出特性讓 Sufficient Context Agent 的回應解析更穩定，建議設計如下 JSON schema：

```json
{
  "sufficient": false,
  "confidence": 0.3,
  "missing_aspects": ["病患過敏資訊", "藥物交互作用"],
  "refined_queries": [
    "patient allergy records post-surgery 2024",
    "drug interaction warfarin aspirin"
  ]
}
```

---

## 8. 資料量對架構規劃的決定性影響

資料量是所有架構決策中最容易被忽略、卻影響最深遠的變數。以下是一個基於資料規模的決策矩陣：

> ⚠️ **維度說明**：架構選型的**主要維度應為 chunk 數與總 token 量**，而非文件份數。1,000 份各 200 頁的 PDF 與 1,000 份單頁備忘錄是完全不同的工程量級。文件份數僅作為粗略參考，請以實際 chunk 數估算。

> ⚠️ **升級路徑警告**：相鄰層（小型→中型、中型→大型）可漸進升級；**跨層（小型→大型）幾乎等於重建**，資料層、檢索層、Harness、模型層四個維度全換。若預期資料量會增長，建議**直接從中型架構起步**，避免日後重寫成本加倍。

### 規模分層決策矩陣

```
資料量規模
    │
    ├── 小型（< 1,000 份文件 / < 100K chunks / < 10MB 純文字）
    │   ├── 推薦架構：LLM Wiki + grep
    │   ├── 理由：直接 grep Markdown，不需向量 DB
    │   ├── Harness：單層迴圈即可，Sufficient Context 邏輯簡單
    │   ├── 模型：Gemma 4 12B（簡單 2–3 跳查詢）
    │   └── ⚠️ 若預期成長，直接用中型架構
    │
    ├── 中型（1,000–50,000 份文件 / 100K–5M chunks / 10MB–1GB）
    │   ├── 推薦架構：LLM Wiki + BM25 + 輕量向量搜尋
    │   ├── 理由：需要語意搜尋補足，但仍可本地化
    │   ├── Harness：雙層迴圈 + query 分類器路由
    │   └── 模型：70B 主推理 + 8B judge（12B 在複雜多跳任務穩定性存疑）
    │
    ├── 大型（> 50,000 份文件 / > 5M chunks / > 1GB）
    │   ├── 推薦架構：分片 Agentic RAG + 混合檢索
    │   ├── 理由：單一向量庫不夠，需要跨語料庫路由
    │   ├── Harness：跨語料庫選庫 + 多來源融合 + GraphRAG
    │   └── 模型：70B 主模型，邊緣節點用 12B
    │
    └── 超大型（數 TB，多系統分散）
        ├── 推薦架構：Federated Agentic RAG
        ├── 理由：無法集中，需要分散式協調
        ├── Harness：多節點協調 + 結果聚合 + 衝突解決
        └── 模型：混合雲（邊緣小模型 + 雲端大模型驗證）
```

### 資料異質性：比資料量更難處理的變數

資料量只是一個維度，資料**異質性**（heterogeneity）才是更深的架構挑戰：

| 資料特性 | 架構影響 |
|----------|----------|
| 純文字 + 關鍵字查詢 | BM25 / grep 優先 |
| PDF + 圖表 | 需要文件解析層（Docling、LlamaParse）|
| 多語言混合 | 需要語言偵測 + 分語言 embedding 模型 |
| 時效性強（每日更新）| LLM Wiki Lint 必須自動化排程 |
| 結構化資料（資料庫表格）| 需要 Text-to-SQL 而非向量搜尋 |
| 程式碼庫 | grep / AST 搜尋優於向量 |

### 資料量與 LLM Wiki 的關係

LLM Wiki 模式在不同規模下的適用性：

- **小型**：整個 wiki 可以完整塞進 Gemma 4 的 128K 上下文，直接問答，不需要任何檢索
- **中型**：wiki 超出上下文，需要在 wiki 頁面之間做輕量檢索
- **大型**：wiki 本身需要分層（子 wiki + 主索引），Planner Agent 先查索引再決定讀哪個子 wiki

---

## 9. 持續學習：檢索的終極邊界

a16z 在 2026 年 4 月的報告中拋出了一個讓所有 RAG 工程師必須面對的根本問題：

> **一個能無限取回資訊的系統，不代表它真正學會了任何東西。**

他們用電影《記憶拼圖》做比喻：Leonard 靠著紙條和刺青記事，但從來沒有真正「學會」任何新東西。現在所有的 RAG 系統，包括最先進的 Agentic RAG，都是 Leonard。

![In-Context Learning 的極限](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2026/04/What-In-Context-Learning-Misses.png)

### 在上下文學習的三個死角

**死角一：真正的新發現**  
費馬最後定理的證明、龐加萊猜想的解法——這類需要真正創造新概念的問題，無法從現有文獻中取回，也無法由更複雜的 RAG 架構解決。

**死角二：隱性知識（Tacit Knowledge）**  
如何從醫學掃描圖辨識良性與惡性腫瘤的細微差異、如何辨識特定說話者的語調——這些知識維度過高，無法用語言表達，也無法被 wiki 頁面捕捉。

**死角三：對抗性適應**  
安全威脅持續演化，系統需要在接觸新攻擊模式的當下就更新判斷能力，不是等到下次訓練週期。

### 學習光譜：從取回到更新

![學習發生在哪裡](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2026/04/Where-does-the-learning-happen_.png)

a16z 繪製出一條完整的學習光譜：

```
Context 端（取回）         Modules（半壓縮）         Weights（全參數更新）
        │                       │                          │
   標準 RAG               LoRA / Adapter              Test-Time Training
   Agentic RAG            附加知識模塊                持續學習（研究前沿）
   LLM Wiki               可組合、不改主模型          Catastrophic Forgetting 未解
        │                       │                          │
   現在可以做             近期可落地                  2–3 年後的技術
```

### 為什麼 Weights 端還沒成熟？

![Naive 權重更新為何失敗](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2026/04/Why-Naive-Weight-Updates-Fail.png)

四個根本性障礙：

1. **災難性遺忘（Catastrophic Forgetting）**：學習新知識會覆蓋原有知識，尚無穩健的解決方案
2. **時間解耦問題（Temporal Disentanglement）**：不變規則和可變事實壓縮在同一批參數中，更新一個會破壞另一個
3. **對齊退化（Alignment Degradation）**：即使是局部良性的微調，也可能廣泛破壞對齊行為
4. **可審計性崩潰（Auditability Breakdown）**：持續更新的模型無法版本化、測試或認證

### 務實的採用建議

![持續學習新創生態](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2026/04/Continual-Learning-Startup-Landscape-v2.png)

對現在的工程師而言，最務實的分層策略：

```
第一層（現在就做）：Agentic RAG + LLM Wiki
第二層（近期考慮）：LoRA adapter 讓模型逐漸內化高頻知識
第三層（等技術成熟）：真正的持續學習，待 Catastrophic Forgetting 有解決方案再評估
```

---

## 10. 地端 LLM 檢索的未來路線圖

整合五個核心來源，可以勾勒出地端 LLM 檢索機制的三年發展路徑：

### 現在（2026）：架構拼圖已齊

所有必要的拼圖已經存在，只是還分散：

```
Gemma 4 12B        → 地端 Agent 能力（多步規劃 + 結構化輸出）
LLM Wiki           → 知識預消化（原始文件噪音的解方）
混合檢索           → grep + BM25 + 向量 + RRF（工程標準答案）
Agentic RAG 框架   → Sufficient Context 終止邏輯
Harness 設計       → 把上面四件事整合成可運作的系統
```

**現在最重要的能力**：把這些拼圖組合起來的 Harness 設計能力。

### 近期（2026–2027）：知識層的精緻化

- LLM Wiki 模式**已出現**可用開源實作：[lucasastorian/llmwiki](https://github.com/lucasastorian/llmwiki)（FTS5 + MCP，⭐ 1.1k）為代表；社群延伸版本（v2 方向）正在加入 Knowledge Graph 與 event-driven 自動化
- 語意 grep 工具（ColGrep、jina-grep）將成為標準工具鏈的一部分
- LoRA adapter 作為 wiki 的「快取加速層」開始落地

### 中期（2027–2028）：Harness 即產品

- Harness 框架將從「工程基礎設施」演化為「可售賣的產品」
- 領域特化的 Agentic RAG 解決方案（法律、醫療、金融）在地端完整可用
- 模型端：12B 等級模型的 Agentic 能力持續提升，70B 模型的門檻降低

### 長期（2028+）：邊界的真正突破

- Continual Learning 的參數更新問題若有突破，RAG 作為外掛記憶體的角色將被重新定義
- 但 a16z 的警告值得銘記：可審計性和隱私保護的需求，會讓「純外掛記憶體」的 RAG 架構在高風險行業持續有其位置

### 給台灣 AI 從業者的三個行動建議

**行動一：先建 LLM Wiki，再談 Agentic**  
在導入複雜的 Agentic RAG 框架之前，先把知識庫整理成結構化 wiki。這一步成本低、效益高，且讓後續所有層次的建設都更容易。

**行動二：用 Gemma 4 12B 驗證地端可行性**  
Gemma 4 12B 是目前最適合地端 Agentic RAG 驗證的模型：開源、明確的 Agent 設計（結構化輸出 + multi-step planning）、E2B 精簡版 < 1.5GB。先在筆電上以量化版本跑通完整流程，再評估是否需要完整精度或更大的模型。

**行動三：Harness 投資優先於模型投資**  
換一個更好的模型，性能提升是線性的。設計一個更好的 Harness（特別是 Sufficient Context 終止邏輯 + 查詢分類路由），性能提升可以是非線性的。已有案例顯示 Harness 重設計在不換模型的前提下帶來數量級的效益差異（詳見 §6 量化證據表）。時間和精力應該優先投入在 Harness 設計上。

---

## 附錄：關鍵圖表索引

| 圖表 | 來源 | URL |
|------|------|-----|
| Agentic RAG 封面 | Google Research | [連結](https://storage.googleapis.com/gweb-research2023-media/original_images/AgenticRAG_Cover.png) |
| Agentic RAG 架構對比 | Google Research | [連結](https://storage.googleapis.com/gweb-research2023-media/original_images/AgenticRAG3_Comparison.png) |
| Gemma 4 Banner | Google Developers | [連結](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/gemma4_banner_2.original.png) |
| In-Context Learning 的極限 | a16z | [連結](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2026/04/What-In-Context-Learning-Misses.png) |
| 學習光譜（Context → Weights）| a16z | [連結](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2026/04/Where-does-the-learning-happen_.png) |
| Transformer vs SSM 比較 | a16z | [連結](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2026/04/Transformers-vs.-SSMs-v2.png) |
| 參數學習方法概覽 | a16z | [連結](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2026/04/Select-Approaches-to-Parametric-Learning.png) |
| Naive 權重更新失敗原因 | a16z | [連結](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2026/04/Why-Naive-Weight-Updates-Fail.png) |
| 持續學習新創生態 | a16z | [連結](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2026/04/Continual-Learning-Startup-Landscape-v2.png) |

---

*本文整合以下來源撰寫：*
- *Google Research Agentic RAG（2026-06-05）*
- *a16z Continual Learning（2026-04-22）*
- *愛好 AI 工程 Blog：Grep 論戰（2026-06-03）*
- *Andrej Karpathy：LLM Wiki Gist*
- *Google Developers：Gemma 4 12B（2026-06-03）*
- *lucasastorian/llmwiki — LLM Wiki 開源實作（GitHub，Apache 2.0）*
- *ai-boost/awesome-harness-engineering — Harness 工程量化彙整（GitHub）*

*事實查核與可行性審查：Claude Opus 4.8（2026-06-07）*
