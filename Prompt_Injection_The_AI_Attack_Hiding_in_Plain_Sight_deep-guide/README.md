# Prompt Injection 深度導讀 — 製作紀錄

## 來源素材

- **逐字稿**：`Prompt_Injection_The_AI_Attack_Hiding_in_Plain_Sight.srt`
- **節目**：The Threat Intelligence Podcast EP3（OWASP GenAI Security Project，2026/6/9）
- **影片**：https://www.youtube.com/watch?v=FDwXMfDHvyo
- **主持與來賓**：Dave Hat（主持，RumRunner Media）、Brian Nakayama 博士、Rachel James（OWASP GenAI「AI Threat Intelligence Initiative」志工負責人）

## 製作流程

1. **深度導讀生成**（`deep-guide` skill）
   - 將 SRT 逐字稿去除時間戳記、合併段落
   - 以「痛點先行 → 靈魂拷問 → 機制解構 → 深層真相 → 落地價值」5 段式敘事改寫成 `Prompt_Injection_深度導讀.md`
   - 主題鎖定 Grok/Bankerbot 摩斯密碼搶案、prompt injection 結構性弱點、間接注入、過度代理權、分級授權建議
   - 文末附上整理過的英文逐字稿全文

2. **標點與格式統一**
   - 全文中文標點由半形改為全形
   - 開頭新增節目資訊 blockquote（節目名稱、主持人、來賓）
   - 確認全文格式一致（中文本文 vs. 英文附錄逐字稿分開處理）

3. **HTML 轉換**（`md_to_html` skill）
   - 評估每個段落是否需要示意圖，產出 4 組共 8 張圖（皆含 16:9 桌面版 + 9:16 手機版）：
     | 圖片 | 對應內容 |
     |---|---|
     | `summary.png` / `summary-mobile.png` | 全文重點「一圖看懂」5 卡片總覽 |
     | `morse-attack.png` / `-mobile.png` | 摩斯密碼攻擊機制：過濾器看字面 vs. AI 懂語意 |
     | `indirect-injection.png` / `-mobile.png` | 間接 prompt injection：隱形文字操弄 AI 推薦 |
     | `tiered-authorization.png` / `-mobile.png` | 把 AI 代理人當「新人」分級授權 |
   - 圖片以 `scripts/codex_imagegen.py` 逐一生成（非並行，避免 codex exec session 衝突）
   - 建立 `index.html`：inline CSS、`#f9f7f4`/`#1a1a1a` 護眼配色、繁中字體堆疊、`text-wrap: balance` 標題、本文寬度 720px、summary banner 置頂、各段落圖以 `<picture>` 切換桌機/手機版本、點擊放大 lightbox、附錄逐字稿以 `<details>` 收合呈現

4. **驗證**
   - `python3 -m html.parser` 語法檢查通過
   - Playwright 截圖 QA：桌面 1280×800、手機 390×844，確認圖片比例、版面排版、lightbox 互動皆正常

## 目錄結構

```
Prompt_Injection_The_AI_Attack_Hiding_in_Plain_Sight_deep-guide/
├── Prompt_Injection_深度導讀.md      # 導讀原文（含附錄逐字稿）
├── index.html                         # 最終發布用 HTML
├── README.md                          # 本檔案
├── images/                            # 8 張示意圖（16:9 + 9:16）
└── qa_*.png                           # Playwright QA 截圖
```
