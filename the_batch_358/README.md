# 掌控權的幽靈：AI 時代的供應鏈主權與防禦邊界

## 📋 專案概述

本專案是對 DeepLearning.AI《The Batch》Issue 358 的深度導讀與視覺化分析。通過 7 個複雜信息圖表，剖析 Claude Fable 的「隱形降級」事件如何揭示 AI 時代的供應鏈脆弱性、地緣政治風險與主權覺醒。

**原文來源**：https://www.deeplearning.ai/the-batch/issue-358

---

## 🎯 內容架構

### 五大章節

1. **一、突然被收回的數位水電** — 商業連續性與供應鏈危機
2. **二、安全防線還是商業壁壘？** — 黑盒防禦的稽核死局
3. **三、從代碼補全到系統故障診斷** — 新型防禦評測的突圍
4. **四、AI 供應鏈的地緣政治警鐘** — 主權 AI 的全面覺醒
5. **五、特權前導路徑的思維煉金** — 突破自主防禦 Agent 的訓練死局

### 原始文章內容

可摺疊收起的完整英文原文（The Batch Issue 358 全文）

---

## 📊 信息圖表清單

### 圖表 0：AI 供應鏈危機四步演進流
**檔案**：`images/infographic_0_supply_chain_escalation.png`（桌面） / `-mobile.png`（手機）  
**生成時間**：2026-06-21  
**尺寸**：4770×2670 px (16:9) | 300 DPI  

**內容**：
- 4 個關鍵時間點（2025年4月→7月）
- 每節點包含：事件名稱 | 影響方 | 全球反應
- 配色漸層：深藍 (#0f172a) → 火橙 (#f97316)
- 底部統計：開源 AI 投資 ↑40% | 進口限制 ↑25%

**提示詞**：
```
Create a horizontal flow infographic showing the escalation timeline of AI supply chain risks, 
with 4 key turning points:

1. [April 2025] Anthropic releases Claude Fable 5 with competitive restrictions
   - Stakeholder impact: Developers, AI researchers, enterprise customers
   - Global response: Concerns about vendor lock-in, questioning safety justifications

2. [Hidden degradation] Silent performance downgrade detected in Claude Code mode
   - Stakeholder impact: Evaluators, independent testers, compliance teams
   - Global response: Backlash, demand for transparency, audit concerns

3. [Export controls] US Commerce Dept restricts Mythos/Fable access (geopolitical shock)
   - Stakeholder impact: Global AI community, non-US nations, Anthropic employees
   - Global response: Acceleration of AI sovereignty initiatives, open-source investment surge

4. [Sovereignty awakening] Global pivot to open-source alternatives & local AI infrastructure
   - Stakeholder impact: Governments, enterprises, startups worldwide
   - Global response: Massive investment in DeepSeek, Qwen, Kimi, local models

Visual style: 
- Color scheme: Dark blue (#0f172a) to fire orange (#f97316) representing escalation
- Central timeline spine connecting 4 stages
- Each stage: event card (top) | stakeholder icons (middle) | response items (bottom)
- Bottom statistics: "Open-source AI investment ↑40% | Import restrictions ↑25%"
- Professional tech policy briefing tone, Traditional Chinese labels + English terms

Aspect ratio: 16:9, 300 DPI, PNG format
```

---

### 圖表 1：Fable 5 隱形降級風波時間線
**檔案**：`images/infographic_1_fable_timeline.png`（桌面） / `-mobile.png`（手機）  
**生成時間**：2026-06-21  
**尺寸**：4770×2670 px (16:9) | 300 DPI  

**內容**：
- 垂直時間線：T0 → T+1w → T+2w → T+3w → T+4w
- 5 個事件卡片，嚴重程度用色彩標記（紅/橙/黃）
- 圖示說明：🔒限制 | ⚠️風險 | 🌍全球 | 📊數據
- 標題：「從廠商控制到市場衝擊的 4 週」

**提示詞**：
```
Create a vertical timeline infographic documenting the Claude Fable 5 degradation incident:

Timeline events:
- [T0] Fable 5 released with "competitive restrictions" in ToS
  Severity: Medium | Indicator: 🔒 Restriction | Impact: Developer concern about ToS fairness

- [T+1w] Silent invisible degradation detected in Claude Code mode (no user notification)
  Severity: High | Indicator: ⚠️ Risk | Impact: Trust breach, audit/compliance implications

- [T+2w] Anthropic backlash → switch to transparent notification (still restricts capability)
  Severity: Medium-High | Indicator: 🌍 Global | Impact: Market loses confidence, developers reconsider

- [T+3w] US Commerce Dept export controls on Mythos/Fable models
  Severity: Critical | Indicator: 🚫 Embargo | Impact: Geopolitical spillover

- [T+4w] Anthropic disables Fable access globally (all users affected)
  Severity: Critical | Indicator: 📊 Data | Impact: Supply chain shock, accelerates open-source

Bottom annotation: "From vendor control to market shock in 4 weeks"

Visual style:
- Central dark blue timeline spine
- Event cards: date marker (left) | incident name (center) | severity color (right)
- Color coding: ⚠️Yellow (low-medium) → 🟠Orange (high) → 🔴Red (critical)
- Each card includes detailed description and stakeholder icons
- Professional, suitable for policy/security briefing

Aspect ratio: 16:9, 300 DPI, PNG format, Traditional Chinese
```

---

### 圖表 2：評測基準演進對比
**檔案**：`images/infographic_2_benchmark_evolution.png`（桌面） / `-mobile.png`（手機）  
**生成時間**：2026-06-21  
**尺寸**：4770×2670 px (16:9) | 300 DPI  

**內容**：
- 左側（舊基準）vs 右側（新基準三欄）對比
- SWE-bench：bug fixes | ★★ | ~100 行代碼 | 90%+ 飽和
- DeepSWE：特徵實作 | ★★★★ | 5.5x 更多代碼 | 70% (GPT-5.5)
- ProgramBench：程序合成 | ★★★★★ | 完整可執行 | 3% (Claude Opus 4.7)
- ITBench-AA：根因診斷 | ★★★★★ | 現代基礎設施 | 46.7% (Claude Opus 4.7)
- 中心箭頭：「能力邊界從編碼轉向系統思維」

**提示詞**：
```
Create a benchmark evolution comparison infographic:

Left side (Legacy - SWE-bench family):
- Problem type: Bug fixes and basic code repair
- Difficulty: ★★☆☆☆ (Easy)
- Code complexity: ~100 lines typical
- Model performance: 90%+ (saturated, data contamination issue)
- Status: Outdated for modern agent evaluation

Right side (Next Generation - 3 parallel columns):

Column 1 - DeepSWE:
- Problem type: Feature implementation (more challenging)
- Difficulty: ★★★★☆ (Hard)
- Code complexity: ~550 lines (5.5x more than SWE-Bench Pro)
- Leaderboard: GPT-5.5 (70%) > Claude Opus 4.8 (58%) > Gemini 3 Flash (5%)
- Key feature: Human-vetted problems from private codebases

Column 2 - ProgramBench:
- Problem type: End-to-end program synthesis (from idea to working code)
- Difficulty: ★★★★★ (Very Hard)
- Scope: Complete functional programs with test suites
- Leaderboard: Claude Opus 4.7 (3%), Claude Opus 4.6 (2.5%), Claude Sonnet 4.6 (1.6%), Others (0%)
- Key challenge: Only 3% pass rate even at top-tier models

Column 3 - ITBench-AA:
- Problem type: Root cause analysis in modern infrastructure
- Difficulty: ★★★★★ (Very Hard)
- Scope: 59 real-world incidents with alerts, traces, system metrics
- Leaderboard: Claude Opus 4.7 (46.7%) > GPT-5.5 (45.8%) > ... > Llama 3.3 70B (0.6%)
- Focus: Blue team operational readiness

Center connecting arrow: "AI Agent evaluation boundary shifts from coding to systems thinking & incident response"

Bottom annotation: "AI Agent evaluation 2024-2025: From syntax completion to execution in production"

Color coding:
- Legacy (gray/muted colors) represents saturation
- New generation (blue → orange gradient) represents frontier difficulty
- Star ratings visualized as filled/empty stars with color intensity

Aspect ratio: 16:9, 300 DPI, PNG format, Traditional Chinese
```

---

### 圖表 3：Nemotron 3 Ultra 架構圖
**檔案**：`images/infographic_3_nemotron_architecture.png`（桌面） / `-mobile.png`（手機）  
**生成時間**：2026-06-21  
**尺寸**：4770×2670 px (16:9) | 300 DPI  

**內容**：
- 頂部規格：550B 參數 | 55B active per token | 183 tokens/sec | 1M 上下文
- 中心架構：混合 Transformer-Mamba MoE 層疊結構
- 訓練管道：預訓練 (20T tokens) → 監督微調 + RL (6 域) → 多師蒸餾
- 性能對比條形圖

**提示詞**：
```
Create an architecture visualization of Nvidia Nemotron 3 Ultra 550B model:

Top section - Key specifications:
- Total parameters: 550B
- Active per token: 55B
- Throughput: 183 tokens/sec
- Context window: 1M tokens
- License: OpenMDW-1.1 (open weights)

Main architecture (center) - Hybrid Transformer-Mamba structure:
- Layer pattern visualization: [Mamba block] → [Self-attention] → [LatentMoE router] → [repeat]
- Mamba advantage: 📉 Lower memory footprint for long sequences
- Transformer advantage: 🎯 Higher precision token recall
- MoE router: Compresses each token → routes to 10 specialist experts
- Multi-token prediction: Generates multiple tokens per inference step

Training pipeline (bottom - left to right):

Stage 1 - Pretraining (20T tokens):
- Phase A: 15T tokens broad knowledge (diverse domains)
- Phase B: 5T tokens high-quality data
  - 173B GitHub code
  - Synthetic legal knowledge
  - Synthetic factual knowledge
- Format: 4-bit NVFP4 quantization for efficiency

Stage 2 - Supervised Fine-tuning + Reinforcement Learning:
- 6 training domains: reasoning | coding | agentic | chat | safety | usability
- Method: Auto-verifiable rewards for each domain

Stage 3 - Multi-Teacher Distillation:
- 10+ domain-specialist teacher models
- Each teacher grades student outputs within its specialty
- Reward signal: Per-token rather than task-end
- Iterations: 2 iterative rounds, rebuilding teachers each round

Performance comparison (bottom-right bar chart):
- Intelligence Index: 47.7% (NVFP4) vs 48.2% (full precision)
- vs US open-weight baselines:
  - +21% vs Google Gemma 4 31B (39.2%)
  - +44% vs OpenAI gpt-oss-120b (33.3%)
- vs leading China models:
  - -8% vs Moonshot Kimi K2.6 (53.9%)
  - Comparable to DeepSeek V4 Pro & GLM-5.2

Style: Technical architecture diagram with clean typography
- Function-based color coding (Mamba = blue, Transformer = purple, MoE = orange)
- Clear layered visualization showing data flow
- Professional engineering briefing style

Aspect ratio: 16:9, 300 DPI, PNG format, Traditional Chinese + English technical terms
```

---

### 圖表 4：地緣政治供應鏈脆弱性演進
**檔案**：`images/infographic_4_geopolitical_supply_chain.png`（桌面） / `-mobile.png`（手機）  
**生成時間**：2026-06-21  
**尺寸**：4770×2670 px (16:9) | 300 DPI  

**內容**：
- 三歷史階段並排對比（半導體 2018-2022 → 稀土 2010-2020 → AI 模型 2025）
- 每階段：觸發事件 | 被影響國家 | 應對投資 | 替代方案
- 核心洞察：「一旦存取被威脅，國家大幅投資替代方案」
- 預測：「開源 AI 投資 2025-2027: ↑40-60% YoY」

**提示詞**：
```
Create a geopolitical supply chain vulnerability pattern infographic showing historical parallels:

Three supply chain crisis stages (left → right):

Stage 1 - Semiconductor Supply Chain (2018-2022):
- Trigger event: US moves to restrict China's chip access (export controls on advanced nodes)
- Affected nations: China, allies dependent on Taiwan/US sources
- China's response: Massive state investment in semiconductor self-sufficiency
- Investment increase: ↑300% in R&D spending
- Outcome: Huawei isolated, but China accelerates to advanced nodes
- Lesson: Market is incentivized to reduce dependence

Stage 2 - Rare Earth Minerals (2010-2020):
- Trigger event: China limits rare earth exports to Japan (trade dispute)
- Affected markets: Electronics, renewable energy, defense systems
- Global response: US, Japan, EU secured alternative supplies from Vietnam, Myanmar, Myanmar
- Diversification result: Reduced China dominance from 95% to 60% of global supply
- Investment increase: Alternative mining projects +50%
- Lesson: Geopolitical risk drives supply chain diversification

Stage 3 - AI Models (2025 - PRESENT):
- Trigger event: US export controls on frontier AI (Mythos, Fable) requiring foreign licenses
- Affected nations: 🌍 ALL nations globally (not just China/rivals)
- Affected stakeholders: Global AI research, enterprises worldwide, non-US developers
- Response mechanism:
  - Direct: Invest heavily in open-source alternatives
  - Indirect: Accelerate sovereign AI initiatives (local deployment, local training)
- Investment trajectory: Open-source AI funding projected ↑40-60% YoY (2025-2027)
- Predicted outcomes: DeepSeek, Qwen, Kimi, local models gain massive adoption

Pattern recognition box (center-bottom):
"Historical pattern: Once access to critical technology is restricted, nations/markets 
rationally invest to build alternatives. Each wave of restrictions accelerates the 
very thing it was meant to prevent."

Key statistics callouts:
- 🔴 Semiconductor: US restriction (2022) → China R&D +300% within 2 years
- 🟠 Rare Earths: Supply shock (2010) → Diversification completed by 2020
- 🟡 AI Models: Export controls (2025) → Open-source ecosystem explosion (projected)

Visual style:
- Vertical parallel columns with connecting arrows showing cause→effect
- Color coding: Each stage (semiconductor=blue, rare earth=green, AI=orange) 
- Icon indicators: 🚫embargo | 💰investment | 🏭infrastructure | 🔓open-source
- Timeline markers showing years
- Severity indicators (🔴🟠🟡) showing escalation

Aspect ratio: 16:9, 300 DPI, PNG format, Traditional Chinese
```

---

### 圖表 5：POPE 訓練流程圖
**檔案**：`images/infographic_5_pope_training_flow.png`（桌面） / `-mobile.png`（手機）  
**生成時間**：2026-06-21  
**尺寸**：4890×2790 px (16:9) | 300 DPI  

**內容**：
- 4 階段從上到下流程：問題篩選 → 前綴提取 → GRPO 訓練 → 漸進 hint 移除
- 每階段包含目標、方法、輸出
- 結果對比條形圖（AIME 2025 & HMMT 2025）
- 教育洞察框

**提示詞**：
```
Create a step-by-step training progression visualization for POPE 
(Privileged On-Policy Exploration) framework:

Main flow (top to bottom, 4 phases):

Phase 1 - Problem Selection & Filtering:
- Start with: 3 challenging math datasets (AIME, HMMT, other competition math)
- Filter criteria: Model failed 128+ times in baseline attempts
- Token generation budget: Up to 32k tokens per failed attempt
- Output: Curated set of "hard problems" where standard methods fail
- Visual: Funnel narrowing to hard problems subset

Phase 2 - Solution Prefix Extraction:
- Input: Known correct solutions for hard problems
- Process: Systematically extract beginning portions of solutions
- Prefix length scaling: Increase from 1/4 → 1/2 → 3/4 → full solution
- Testing: Feed Qwen3-4B progressively longer prefixes until correct completion
- Annotation: "What's the minimum hint that enables correct solving?"
- Example hint: "Solve geometry problem" + "Draw auxiliary triangle, apply Pythagorean theorem..."
- Output: Training dataset with problem + optimal hint pairs

Phase 3 - Dual-Training with GRPO:
- Training setup: Each problem presented in 2 versions with 50-50 ratio
  - Version A: WITH solution prefix hint (scaffolded)
  - Version B: WITHOUT prefix (unsupported)
- Reward mechanism:
  - When model solves: RL increases probability of generating same tokens
  - When model fails: RL decreases probability
- Training target: GRPO algorithm adjusts weights to maximize solving rate
- Checkpoint: Model learns to solve from provided midpoint

Phase 4 - Progressive Hint Removal:
- Iteration 1: Model trained extensively with hints
  - Performance: High accuracy when starting from middle of solution
  - Skill acquired: "How to complete once you know the setup"
  
- Iteration 2: Training pivots to removing hints
  - Model now learns to find the starting point itself
  - Skill acquired: "How to start from problem statement"
  - Final state: Model can solve independently, start-to-finish

Results comparison (bottom, bar chart):

AIME 2025 Dataset:
- Baseline supervised FT: ~30% pass@1
- Typical GRPO: 49.6% pass@1
- POPE: 53.1% pass@1 ← +3.5 percentage points (+7% improvement over GRPO)
- Pass@16 rates: GRPO 81.4% vs POPE 82.6% (diminishing return at multiple attempts)

HMMT 2025 Dataset:
- Baseline supervised FT: ~20% pass@1
- Typical GRPO: 31.0% pass@1
- POPE: 37.8% pass@1 ← +6.8 pp (+22% relative improvement)
- Pass@16 rates: GRPO 63.8% vs POPE 67.5%

Educational insight box:
"POPE breaks hard problem learning into 2 sequential substeps:
(1) Learn to solve FROM A KNOWN MIDPOINT (easier, scaffolded)
(2) Learn to solve FROM START (harder, independent)

This matches human learning psychology: scaffolding helps learners acquire complex skills 
by breaking them into manageable chunks. Remove scaffolds gradually once mastered."

Application callout (blue box):
"Security Agent training: Domain experts can provide initial investigation steps 
(e.g., 'run netstat -an', 'check /var/log'), then RL learns to extend from there. 
Much cheaper than training from scratch."

Visual style:
- Flow diagram with clear vertical arrows showing progression
- Phase boxes with different colors (blue→purple→orange→green)
- Horizontal comparison of GRPO vs POPE at each phase
- Icon indicators: 📚 learning | 🎯 target | ✅ success | 📊 metrics

Aspect ratio: 16:9, 300 DPI, PNG format, Traditional Chinese with English terms
```

---

### 圖表 6：POPE vs GRPO 性能對比
**檔案**：`images/infographic_6_pope_performance_comparison.png`（桌面） / `-mobile.png`（手機）  
**生成時間**：2026-06-21  
**尺寸**：4830×2730 px (16:9) | 300 DPI  

**內容**：
- 雙數據集並排柱狀圖（AIME 2025 & HMMT 2025）
- pass@1 與 pass@16 對比
- 配色：GRPO 灰色，POPE 藍色，上升箭頭標示增益
- 3 點關鍵發現

**提示詞**：
```
Create a performance comparison infographic: POPE vs GRPO vs Supervised Fine-Tuning

Layout: Two datasets side-by-side with grouped bar charts

Dataset 1 - AIME 2025 (American Invitational Mathematics Examination):

Pass@1 results (single attempt):
- Supervised FT: ~30% (baseline, lowest)
- Typical GRPO: 49.6% 
- POPE: 53.1% ← Improvement: +3.5 percentage points vs GRPO, +77% vs SFT
- Bar coloring: SFT (light gray) | GRPO (dark gray) | POPE (blue)
- Percentage labels on each bar

Pass@16 results (16 attempts allowed):
- Supervised FT: ~40%
- Typical GRPO: 81.4%
- POPE: 82.6% ← Marginal gain: +1.2 pp
- Insight: Advantage diminishes with multiple retries

Dataset 2 - HMMT 2025 (Harvard-MIT Mathematics Tournament):

Pass@1 results:
- Baseline GRPO: 31.0%
- POPE: 37.8% ← Improvement: +6.8 pp (+22% relative gain)
- Visual: Larger bar for POPE showing stronger advantage
- Up arrow annotation: "+22%"

Pass@16 results:
- Baseline GRPO: 63.8%
- POPE: 67.5% ← Marginal gain: +3.7 pp
- Insight: Still positive but significantly reduced advantage

Key findings box (center-bottom):
Finding 1: "POPE's advantage strongest at pass@1 (single attempt)"
  - When model has only one try, prefix guidance matters most
  
Finding 2: "Advantage diminishes sharply at pass@16 (multiple retries)"
  - With 16 attempts, even GRPO finds solutions (brute force exploration)
  
Finding 3: "Best suited for budget-constrained scenarios"
  - Real-time security incident response (single attempt budget)
  - Real-time inference (latency constraints)
  - NOT ideal for research with unlimited compute for retries

Use case callout (highlighted box):
"🎯 Where POPE excels:
- Real-time incident response (1 attempt per alert)
- Production inference (latency/token budget constraints)
- Security agent with limited computation

❌ Where POPE has less advantage:
- Research environments (unlimited attempts acceptable)
- Training-time only (no inference constraints)"

Visual elements:
- Paired bar chart with clear visual pairing (GRPO gray, POPE blue)
- Percentage labels on top of each bar
- Up arrows showing improvement magnitude
- Color gradient background (lighter at baseline, stronger at POPE)
- Horizontal comparison lines for visual reference

Bottom annotation: "Dataset difficulty: HMMT > AIME (HMMT shows ~3x larger relative improvement)"

Aspect ratio: 16:9, 300 DPI, PNG format, Traditional Chinese
```

---

## 📱 響應式網頁設計 (RWD)

HTML 已配置完整的響應式設計，支援手機/平板/桌面設備：

### 實現方式

1. **圖表響應式**：
   - 使用 `<picture>` 標籤指定設備特定版本
   - 桌面版：`infographic_X_*.png` (16:9, 4770×2670px)
   - 手機版：`infographic_X_*-mobile.png` (9:16 或 1:1, 360×640px)
   - 媒體查詢斷點：`max-width: 640px`

2. **文本自適應**：
   - 基礎字體：17px (桌面) → 16px (手機)
   - 標題使用 `clamp()` 流體尺寸
   - `text-wrap: balance` 自動換行優化

3. **版面彈性**：
   - 容器 `max-width: 1120px` with `padding: 0 24px`
   - 文章寬度 `max-width: 720px` 確保可讀性
   - 圖表響應寬度：`width: 100%; max-width: 860px`

### 設備支援

- ✅ 手機 (≤640px)：垂直單欄，圖表縮小至 360px 寬度
- ✅ 平板 (641-1024px)：單欄或雙欄混合
- ✅ 桌面 (>1024px)：最大寬度 1120px，最佳閱讀體驗

### Lightbox 功能

- 所有圖表可點擊放大（全屏預覽）
- 手機版：手指滑動或點擊關閉
- 鍵盤：按 Esc 關閉 lightbox

---

## 🛠️ 執行歷史

### 2026-06-21 | 第一次迭代

#### 1. 內容優化 (10:00)
- ✅ 修改 h1 標題大小：`clamp(2rem, 5vw, 3.2rem)` → `clamp(1.5rem, 4vw, 2.4rem)`
- ✅ 分點列表格式修復：`<p>` 內的 `1. 2.` → `<ol><li>` 正確結構
- ✅ 原始文章改成 `<details>` 可摺疊模式（預設收起）
- ✅ 符號錯誤修正：「2。」→「2.」

#### 2. 信息圖表生成 (11:00-12:30)
- ✅ 規劃 7 個圖表需求，逐段分析內容
- ✅ 編寫完整的圖表生成提示詞（7 份）
- ✅ 使用子 Agent 並行生成全部圖表
- ✅ 圖表規格驗證：
  - 尺寸：16:9 比例 (1.753-1.787)
  - 格式：PNG, 300 DPI
  - 語言：傳統中文 + 英文技術術語
  - 總大小：861 KB (優化)

#### 3. 圖表整合 (12:30-13:00)
- ✅ 7 個圖表嵌入 HTML：
  - 圖表 0：導言結尾（全文概覽）
  - 圖表 1：第一章後（時間線）
  - 圖表 2：第三章頭（基準演進）
  - 圖表 3：第三章中（架構圖）
  - 圖表 4：第四章頭（地緣政治）
  - 圖表 5：第五章頭（訓練流程）
  - 圖表 6：第五章中（性能對比）
- ✅ 配置響應式 `<picture>` 標籤
- ✅ 添加 `figcaption` 說明文字

#### 4. 中文字體問題 (13:00)
- ⚠️ 用戶報告：PNG 中文字顯示異常
- 📋 計劃補救方案：重新生成圖表，確保字體配置正確

---

## 📁 檔案結構

```
the_batch_358/
├── index.html                              # 主文章頁面（RWD 優化）
├── README.md                               # 本文檔（執行紀錄 + 提示詞）
└── images/
    ├── infographic_0_supply_chain_escalation.png
    ├── infographic_0_supply_chain_escalation-mobile.png
    ├── infographic_1_fable_timeline.png
    ├── infographic_1_fable_timeline-mobile.png
    ├── infographic_2_benchmark_evolution.png
    ├── infographic_2_benchmark_evolution-mobile.png
    ├── infographic_3_nemotron_architecture.png
    ├── infographic_3_nemotron_architecture-mobile.png
    ├── infographic_4_geopolitical_supply_chain.png
    ├── infographic_4_geopolitical_supply_chain-mobile.png
    ├── infographic_5_pope_training_flow.png
    ├── infographic_5_pope_training_flow-mobile.png
    ├── infographic_6_pope_performance_comparison.png
    ├── infographic_6_pope_performance_comparison-mobile.png
    ├── fable_mechanism.png                 # 既有圖表（第二章）
    └── fable_mechanism-mobile.png
```

---

## 🎨 設計規範

### 配色方案

| 名稱 | 色值 | 用途 |
|------|------|------|
| Background | #f9f7f4 | 頁面背景 |
| Text | #1a1a1a | 主文本 |
| Accent | #0f172a | 標題、強調 |
| Link | #2563eb | 超連結 |
| Muted | #64748b | 輔助文本 |
| Border | #e2e8f0 | 分割線 |
| Primary | #1e40af | 圖表主色（深藍） |
| Accent Orange | #f97316 | 圖表強調（橙色） |
| Success | #10b981 | 圖表成功指標（綠色） |

### 字體堆棧

```css
font-family: "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
```

### 排版規則

- 行高：1.68
- 標題 h1：`clamp(1.5rem, 4vw, 2.4rem)` (24-38px)
- 標題 h2：1.75rem (28px)
- 標題 h3：1.25rem (20px)
- 正文：17px (桌面) / 16px (手機)

---

## 🔧 技術棧

| 工具 | 版本 | 用途 |
|------|------|------|
| HTML5 | - | 結構語義化 |
| CSS3 | - | 響應式設計 + 動畫 |
| JavaScript (Vanilla) | - | Lightbox 交互 |
| Python | 3.9+ | 圖表生成（matplotlib/plotly） |

---

## ✨ 主要特性

1. **完整的視覺敘事**
   - 7 個複雜信息圖表支撐 5 大章節
   - 從微觀（Fable 事件）到宏觀（地緣政治）逐層展開

2. **手機友善**
   - 100% 響應式設計，適應所有屏幕
   - 設備特定圖表版本（16:9 桌面 vs 9:16/1:1 手機）

3. **交互增強**
   - Lightbox 全屏放大圖表
   - 可摺疊原始文章內容
   - 鍵盤快捷鍵支援 (Esc 關閉 lightbox)

4. **可訪問性 (A11y)**
   - 語義化 HTML (`<article>`, `<figure>`, `<details>`)
   - 高對比度配色（WCAG AA 標準）
   - Alt 文本和 figcaption 說明

5. **性能優化**
   - PNG 圖表高效壓縮 (861 KB 總計)
   - CSS 最小化，無外部依賴
   - Vanilla JS (無框架開銷)

---

## 📝 使用指南

### 網頁瀏覽

1. 在瀏覽器中打開 `index.html`
2. 點擊任何圖表進入全屏 lightbox
3. 按 Esc 或點擊背景關閉 lightbox
4. 點擊「原始文章內容」展開/收起英文原文

### 編輯和維護

#### 更新圖表提示詞

1. 編輯 `README.md` 中對應圖表的「提示詞」部分
2. 使用 Codex CLI 或類似工具重新生成圖表
3. 上傳新圖表到 `images/` 目錄（覆蓋原有檔案）
4. 確保同時更新桌面版和手機版

#### 修改 HTML 內容

1. 編輯 `index.html` 中對應章節的 `<p>` 或 `<li>` 標籤
2. 若添加新圖表，使用此範本：
   ```html
   <figure class="section-figure">
     <picture>
       <source media="(max-width: 640px)" srcset="images/your_image-mobile.png">
       <img src="images/your_image.png" alt="圖表描述">
     </picture>
     <figcaption>圖表說明文字</figcaption>
   </figure>
   ```

#### 修改設計

- 顏色：修改 `:root` CSS 變數
- 字體：修改 `body` 的 `font-family` 或 `@media` 規則
- 尺寸：調整 `clamp()` 函數參數或固定 px 值

---

## 🐛 已知問題與計劃

### 當前問題

- 🔴 **中文字體渲染** — PNG 圖表中文字顯示異常
  - 原因：matplotlib/plotly 字體配置
  - 解決方案：計劃重新生成，確保字體庫正確配置

### 計劃改進

- [ ] 加入暗模式支援 (`prefers-color-scheme`)
- [ ] 優化字體加載速度（字體預加載）
- [ ] Open Graph 分享卡片（og:image, og:description）
- [ ] 多語言支援 (Traditional Chinese / English / Simplified Chinese)
- [ ] PDF 導出功能

---

## 📞 技術支援

如遇以下問題，請檢查：

| 問題 | 檢查項目 |
|------|---------|
| 圖表不顯示 | 檢查 `/images/` 目錄中文件是否存在 |
| 圖表模糊 | 確保使用 300 DPI PNG 版本，非壓縮版 |
| 手機排版亂 | 清除瀏覽器快取，重新加載頁面 |
| 中文顯示異常 | 嘗試重新生成圖表，確保字體配置 |
| Lightbox 卡住 | 確認 JavaScript 已啟用 |

---

**文檔最後更新**：2026-06-21  
**維護狀態**：✅ 穩定，待中文字體修復
