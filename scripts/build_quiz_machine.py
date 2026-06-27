from __future__ import annotations

import json
import re
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ("part1", "AI-900_part1_268題.html", "Part 1"),
    ("part2", "AI-900_part2_119題.html", "Part 2"),
    ("part3", "AI-900_part3_88題.html", "Part 3"),
]

OUTLINE_LABELS = {
    "outline-1": "AI 工作負載與負責任 AI",
    "outline-2": "Azure 機器學習基本原則",
    "outline-3": "Azure 電腦視覺工作負載",
    "outline-4": "Azure 自然語言處理工作負載",
    "outline-5": "生成式 AI 與 Azure OpenAI",
}


def clean_soup_html(soup):
    for tag in soup.find_all(["script", "style", "button"]):
        tag.decompose()
    for tag in soup.find_all(True):
        for attr in list(tag.attrs):
            if attr.lower().startswith("on"):
                del tag.attrs[attr]
        if tag.name == "input":
            tag.attrs.pop("checked", None)
            tag.attrs.pop("name", None)
            tag.attrs.pop("id", None)
            tag.attrs["disabled"] = ""
    return str(soup)


def text_of(node) -> str:
    return re.sub(r"\s+", " ", node.get_text(" ", strip=True)).strip() if node else ""


def option_value(input_tag, index: int) -> str:
    value = input_tag.get("value")
    if value and value != "on":
        return value
    input_id = input_tag.get("id", "")
    match = re.search(r"([a-zA-Z])$", input_id)
    if match:
        return match.group(1).upper()
    return str(index + 1)


def option_label(li, input_tag) -> str:
    li_copy = BeautifulSoup(str(li), "html.parser")
    found = li_copy.find("input")
    if found:
        found.decompose()
    label = li_copy.find("label")
    if label:
        return "".join(str(child) for child in label.contents).strip()
    li_node = li_copy.find("li")
    if li_node:
        return "".join(str(child) for child in li_node.contents).strip()
    return clean_soup_html(li_copy).strip()


def infer_type(title: str, inputs) -> str:
    lowered = title.lower()
    if "配對" in title:
        return "matching"
    if "填充" in title or "下拉" in title:
        return "fill"
    if any(inp.get("type") == "checkbox" for inp in inputs):
        return "multiple"
    if any(inp.get("type") == "radio" for inp in inputs):
        return "single"
    if "是非" in title:
        return "truefalse"
    if lowered:
        return "review"
    return "review"


def build_questions() -> list[dict]:
    questions = []
    sequence = 1
    for source_key, filename, source_label in SOURCES:
        soup = BeautifulSoup((ROOT / filename).read_text(encoding="utf-8"), "html.parser")
        for local_index, card in enumerate(soup.select(".question-card"), start=1):
            card_id = card.get("id") or f"{source_key}-{local_index}"
            categories = (card.get("data-category") or "").split()
            meta = text_of(card.select_one(".question-meta"))
            title_node = card.select_one(".question-title")
            title = text_of(title_node)
            original_title = title_node.get("data-original-title", "").strip() if title_node else ""
            if not title or title.startswith("#"):
                title = original_title or f"#{local_index}"

            body = card.select_one(".question-body")
            answer = card.select_one(".answer-content")
            body_copy = BeautifulSoup(str(body or ""), "html.parser")
            inputs = body_copy.select("input")
            selectable_inputs = [
                inp for inp in inputs if inp.get("type") in {"radio", "checkbox"}
            ]
            options = []
            correct_values = []

            for index, inp in enumerate(selectable_inputs):
                li = inp.find_parent("li")
                if not li:
                    continue
                value = option_value(inp, index)
                label_html = option_label(li, inp)
                options.append({"value": value, "html": label_html})
                if inp.has_attr("checked"):
                    correct_values.append(value)

            question_type = infer_type(title, selectable_inputs)
            for ul in body_copy.select("ul"):
                if ul.select("input[type=radio], input[type=checkbox]"):
                    ul.decompose()

            auto_gradable = bool(options and correct_values)
            questions.append(
                {
                    "id": f"{source_key}-{card_id}",
                    "number": sequence,
                    "source": source_label,
                    "sourceFile": filename,
                    "sourceIndex": local_index,
                    "title": title,
                    "type": question_type,
                    "categories": categories,
                    "meta": meta,
                    "stemHtml": clean_soup_html(body_copy),
                    "fullQuestionHtml": clean_soup_html(BeautifulSoup(str(body or ""), "html.parser")),
                    "answerHtml": clean_soup_html(BeautifulSoup(str(answer or ""), "html.parser")),
                    "options": options,
                    "correctValues": sorted(correct_values),
                    "autoGradable": auto_gradable,
                }
            )
            sequence += 1
    return questions


def build_html(questions: list[dict]) -> str:
    data_json = json.dumps(
        {"questions": questions, "outlineLabels": OUTLINE_LABELS},
        ensure_ascii=False,
        separators=(",", ":"),
    )
    return f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI-900 考前刷題機</title>
<style>
:root {{
  --bg: #f6f7fb;
  --panel: #ffffff;
  --ink: #172033;
  --muted: #5e6a7e;
  --line: #dce3ee;
  --blue: #0f6cbd;
  --green: #11845b;
  --red: #c2413b;
  --amber: #9a5b00;
  --violet: #6d4aff;
  --shadow: 0 10px 28px rgba(19, 35, 61, .08);
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans TC", Arial, sans-serif;
  color: var(--ink);
  background: var(--bg);
  line-height: 1.65;
}}
button, input, select {{ font: inherit; }}
a {{ color: var(--blue); text-decoration: none; }}
.app-shell {{
  min-height: 100vh;
  display: grid;
  grid-template-columns: minmax(260px, 320px) minmax(0, 1fr);
}}
.sidebar {{
  position: sticky;
  top: 0;
  height: 100vh;
  overflow: auto;
  padding: 22px;
  background: #eef3f9;
  border-right: 1px solid var(--line);
}}
.brand h1 {{ margin: 0 0 6px; font-size: 1.45rem; line-height: 1.25; }}
.brand p {{ margin: 0 0 18px; color: var(--muted); font-size: .95rem; }}
.countdown {{
  padding: 12px;
  background: #fff7e6;
  border: 1px solid #ffd891;
  border-radius: 8px;
  color: #573700;
  font-weight: 700;
  margin-bottom: 16px;
}}
.control-group {{ margin: 18px 0; }}
.control-group h2 {{
  margin: 0 0 8px;
  font-size: .88rem;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: .04em;
}}
.control-stack {{ display: grid; gap: 8px; }}
.mode-btn, .outline-btn, .action-btn {{
  width: 100%;
  border: 1px solid var(--line);
  background: var(--panel);
  color: var(--ink);
  border-radius: 8px;
  padding: 10px 12px;
  text-align: left;
  cursor: pointer;
}}
.mode-btn.active, .outline-btn.active {{
  border-color: var(--blue);
  background: #e8f3ff;
  color: #074c86;
  font-weight: 700;
}}
.action-btn {{ text-align: center; font-weight: 700; }}
.action-btn.primary {{ background: var(--blue); border-color: var(--blue); color: white; }}
.action-btn.danger {{ color: var(--red); }}
.stats-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
}}
.stat {{
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 10px;
}}
.stat b {{ display: block; font-size: 1.25rem; }}
.stat span {{ color: var(--muted); font-size: .84rem; }}
.main {{
  padding: 24px;
  max-width: 1100px;
  width: 100%;
  margin: 0 auto;
}}
.topbar {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  margin-bottom: 16px;
}}
.topbar h2 {{ margin: 0; font-size: 1.35rem; }}
.topbar-actions {{ display: flex; gap: 8px; flex-wrap: wrap; justify-content: flex-end; }}
.pill {{
  display: inline-flex;
  align-items: center;
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 4px 10px;
  background: white;
  color: var(--muted);
  font-size: .88rem;
}}
.question-card {{
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
  box-shadow: var(--shadow);
  overflow: hidden;
}}
.question-head {{
  padding: 18px 20px;
  border-bottom: 1px solid var(--line);
  display: flex;
  justify-content: space-between;
  gap: 14px;
  align-items: flex-start;
}}
.question-title {{ margin: 0; font-size: 1.22rem; line-height: 1.35; }}
.question-meta {{ color: var(--muted); font-size: .92rem; margin-top: 6px; }}
.question-body {{ padding: 20px; }}
.question-body p:first-child {{ margin-top: 0; }}
.options {{ display: grid; gap: 10px; margin-top: 16px; }}
.option {{
  display: grid;
  grid-template-columns: 24px minmax(0, 1fr);
  gap: 10px;
  align-items: start;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 12px;
  cursor: pointer;
  background: #fbfcff;
}}
.option:hover {{ border-color: #9fc6ee; }}
.option input {{ margin-top: 4px; width: 18px; height: 18px; accent-color: var(--blue); }}
.option.correct {{ border-color: #8fd6b7; background: #edfdf6; }}
.option.wrong {{ border-color: #f0aaa6; background: #fff1f0; }}
.card-actions {{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 10px;
  padding: 16px 20px;
  border-top: 1px solid var(--line);
  background: #fbfcff;
}}
.button-row {{ display: flex; gap: 8px; flex-wrap: wrap; }}
.btn {{
  border: 1px solid var(--line);
  background: white;
  color: var(--ink);
  border-radius: 8px;
  padding: 9px 14px;
  cursor: pointer;
  font-weight: 700;
}}
.btn.primary {{ background: var(--blue); border-color: var(--blue); color: white; }}
.btn.ghost.active {{ background: #fff4cf; border-color: #e9bb43; color: #684200; }}
.feedback {{
  margin-top: 16px;
  border-radius: 8px;
  padding: 12px;
  font-weight: 700;
  display: none;
}}
.feedback.show {{ display: block; }}
.feedback.correct {{ background: #edfdf6; color: var(--green); border: 1px solid #8fd6b7; }}
.feedback.wrong {{ background: #fff1f0; color: var(--red); border: 1px solid #f0aaa6; }}
.feedback.review {{ background: #f4f0ff; color: var(--violet); border: 1px solid #c6b9ff; }}
.answer-panel {{
  display: none;
  margin-top: 16px;
  padding: 16px;
  border-radius: 8px;
  border: 1px solid var(--line);
  background: #f9fbff;
}}
.answer-panel.show {{ display: block; }}
.answer-panel .answer, .answer-panel .rationale, .answer-panel .exam-tip {{
  margin-bottom: 12px;
}}
.progress-line {{
  height: 10px;
  background: #dfe7f2;
  border-radius: 999px;
  overflow: hidden;
  margin: 12px 0 4px;
}}
.progress-line > div {{ height: 100%; background: var(--blue); width: 0; }}
.weak-list {{ display: grid; gap: 8px; }}
.weak-item {{
  display: flex;
  justify-content: space-between;
  gap: 10px;
  padding: 9px 10px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: white;
  font-size: .9rem;
}}
.note-links {{
  display: grid;
  gap: 8px;
  margin-top: 12px;
}}
.note-links a {{
  display: block;
  background: white;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 9px 10px;
}}
.empty {{
  background: white;
  border: 1px dashed var(--line);
  border-radius: 8px;
  padding: 28px;
  text-align: center;
  color: var(--muted);
}}
.keyword-highlight {{ background: rgba(250, 204, 21, .28); border-radius: 4px; padding: 0 .2em; }}
.chinese-noun {{ color: #075ec7; font-weight: 700; }}
.eng-word {{ color: #c52828; font-weight: 700; }}
.eng-abbr {{ color: #7b2cbf; font-weight: 700; }}
table {{ width: 100%; border-collapse: collapse; display: block; overflow-x: auto; }}
td, th {{ border: 1px solid var(--line); padding: 8px; }}
@media (max-width: 860px) {{
  .app-shell {{ display: block; }}
  .sidebar {{ position: static; height: auto; border-right: 0; border-bottom: 1px solid var(--line); }}
  .main {{ padding: 16px; }}
  .topbar, .question-head {{ display: block; }}
  .topbar-actions {{ justify-content: flex-start; margin-top: 10px; }}
  .card-actions {{ display: grid; }}
}}
</style>
</head>
<body>
<div class="app-shell">
  <aside class="sidebar">
    <div class="brand">
      <h1>AI-900 考前刷題機</h1>
      <p>475 題整合練習，單選/複選自動判分，問答題自我核對。</p>
    </div>
    <div class="countdown" id="countdown">考試倒數計算中</div>
    <div class="control-group">
      <h2>刷題模式</h2>
      <div class="control-stack" id="modeControls"></div>
    </div>
    <div class="control-group">
      <h2>命題大綱</h2>
      <div class="control-stack" id="outlineControls"></div>
    </div>
    <div class="control-group">
      <h2>進度</h2>
      <div class="stats-grid">
        <div class="stat"><b id="statDone">0</b><span>已練習</span></div>
        <div class="stat"><b id="statRate">0%</b><span>自動判分答對率</span></div>
        <div class="stat"><b id="statWrong">0</b><span>錯題</span></div>
        <div class="stat"><b id="statFav">0</b><span>收藏</span></div>
      </div>
      <div class="progress-line"><div id="progressBar"></div></div>
    </div>
    <div class="control-group">
      <h2>弱點補強</h2>
      <div class="weak-list" id="weakList"></div>
      <div class="note-links">
        <a href="memory.html">打開關鍵速讀</a>
        <a href="AI-900_part4.html">打開重點整理 Part 4</a>
        <a href="articles/《AI-900》證照考試準備心得與筆記分享_-_系列文章.html">打開系列文章入口</a>
      </div>
    </div>
    <div class="control-group">
      <button class="action-btn primary" id="shuffleBtn">重新隨機此模式</button>
      <button class="action-btn danger" id="resetBtn">清除本機進度</button>
    </div>
    <p><a href="index.html">返回首頁</a></p>
  </aside>
  <main class="main">
    <div class="topbar">
      <div>
        <h2 id="sessionTitle">全部隨機</h2>
        <div id="sessionMeta" class="pill">0 / 0</div>
      </div>
      <div class="topbar-actions">
        <span class="pill" id="typePill">題型</span>
        <span class="pill" id="sourcePill">來源</span>
      </div>
    </div>
    <section id="quizArea"></section>
  </main>
</div>
<script id="quiz-data" type="application/json">{data_json}</script>
<script>
const DATA = JSON.parse(document.getElementById('quiz-data').textContent);
const QUESTIONS = DATA.questions;
const OUTLINE_LABELS = DATA.outlineLabels;
const STORE_KEY = 'ai900_quiz_machine_v1';
const EXAM_TIME = new Date('2026-06-30T16:45:00+08:00');
const TYPE_LABELS = {{ single: '單選題', multiple: '複選題', matching: '配對題', fill: '填充題', truefalse: '是非題', review: '自我核對' }};
const MODES = [
  ['all', '全部隨機'],
  ['wrong', '錯題複習'],
  ['unanswered', '未答題'],
  ['favorites', '收藏題'],
  ['review', '自我核對題']
];
let state = loadState();
let mode = 'all';
let outline = 'all';
let session = [];
let current = 0;
let submitted = false;

function loadState() {{
  try {{
    const parsed = JSON.parse(localStorage.getItem(STORE_KEY) || '{{}}');
    return {{ answers: parsed.answers || {{}}, favorites: parsed.favorites || {{}}, seed: parsed.seed || Date.now() }};
  }} catch {{
    return {{ answers: {{}}, favorites: {{}}, seed: Date.now() }};
  }}
}}
function saveState() {{ localStorage.setItem(STORE_KEY, JSON.stringify(state)); }}
function shuffle(items) {{
  const copy = [...items];
  for (let i = copy.length - 1; i > 0; i--) {{
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }}
  return copy;
}}
function sameSet(a, b) {{
  return a.length === b.length && [...a].sort().every((value, index) => value === [...b].sort()[index]);
}}
function answerFor(q) {{ return state.answers[q.id]; }}
function filteredQuestions() {{
  return QUESTIONS.filter(q => {{
    if (outline !== 'all' && !q.categories.includes(outline)) return false;
    const saved = answerFor(q);
    if (mode === 'wrong') return saved && saved.autoGradable && saved.correct === false;
    if (mode === 'unanswered') return !saved;
    if (mode === 'favorites') return state.favorites[q.id];
    if (mode === 'review') return !q.autoGradable;
    return true;
  }});
}}
function newSession(keepFirst = false) {{
  const previous = session[current]?.id;
  session = shuffle(filteredQuestions());
  if (keepFirst && previous) {{
    const index = session.findIndex(q => q.id === previous);
    if (index > 0) [session[0], session[index]] = [session[index], session[0]];
  }}
  current = 0;
  submitted = false;
  render();
}}
function setMode(next) {{
  mode = next;
  document.querySelectorAll('.mode-btn').forEach(btn => btn.classList.toggle('active', btn.dataset.mode === mode));
  newSession();
}}
function setOutline(next) {{
  outline = next;
  document.querySelectorAll('.outline-btn').forEach(btn => btn.classList.toggle('active', btn.dataset.outline === outline));
  newSession();
}}
function renderControls() {{
  document.getElementById('modeControls').innerHTML = MODES.map(([id, label]) => `<button class="mode-btn ${{id === mode ? 'active' : ''}}" data-mode="${{id}}">${{label}}</button>`).join('');
  const outlines = [['all', '全部大綱'], ...Object.entries(OUTLINE_LABELS)];
  document.getElementById('outlineControls').innerHTML = outlines.map(([id, label]) => {{
    const count = id === 'all' ? QUESTIONS.length : QUESTIONS.filter(q => q.categories.includes(id)).length;
    return `<button class="outline-btn ${{id === outline ? 'active' : ''}}" data-outline="${{id}}">${{label}} (${{count}})</button>`;
  }}).join('');
  document.querySelectorAll('.mode-btn').forEach(btn => btn.addEventListener('click', () => setMode(btn.dataset.mode)));
  document.querySelectorAll('.outline-btn').forEach(btn => btn.addEventListener('click', () => setOutline(btn.dataset.outline)));
}}
function renderStats() {{
  const answers = Object.values(state.answers);
  const auto = answers.filter(a => a.autoGradable);
  const correct = auto.filter(a => a.correct).length;
  const wrong = auto.filter(a => a.correct === false).length;
  document.getElementById('statDone').textContent = answers.length;
  document.getElementById('statRate').textContent = auto.length ? `${{Math.round(correct / auto.length * 100)}}%` : '0%';
  document.getElementById('statWrong').textContent = wrong;
  document.getElementById('statFav').textContent = Object.keys(state.favorites).length;
  document.getElementById('progressBar').style.width = `${{Math.min(100, answers.length / QUESTIONS.length * 100)}}%`;
  renderWeakList();
}}
function renderWeakList() {{
  const rows = Object.entries(OUTLINE_LABELS).map(([id, label]) => {{
    const qs = QUESTIONS.filter(q => q.categories.includes(id));
    const answered = qs.map(q => answerFor(q)).filter(a => a && a.autoGradable);
    const wrong = answered.filter(a => a.correct === false).length;
    const rate = answered.length ? Math.round((answered.length - wrong) / answered.length * 100) : null;
    return {{ id, label, wrong, answered: answered.length, rate }};
  }}).sort((a, b) => b.wrong - a.wrong || (a.rate ?? 101) - (b.rate ?? 101));
  document.getElementById('weakList').innerHTML = rows.slice(0, 5).map(row => `<div class="weak-item"><span>${{row.label}}</span><b>${{row.answered ? `${{row.rate}}% / 錯 ${{row.wrong}}` : '未練'}}</b></div>`).join('');
}}
function render() {{
  renderStats();
  const title = MODES.find(([id]) => id === mode)?.[1] || '全部隨機';
  const outlineText = outline === 'all' ? '' : ` · ${{OUTLINE_LABELS[outline]}}`;
  document.getElementById('sessionTitle').textContent = `${{title}}${{outlineText}}`;
  document.getElementById('sessionMeta').textContent = session.length ? `${{current + 1}} / ${{session.length}} 題` : '0 / 0 題';
  const area = document.getElementById('quizArea');
  if (!session.length) {{
    area.innerHTML = '<div class="empty">這個模式目前沒有題目。可以切回全部隨機，或先完成更多題目後再看錯題與未答題。</div>';
    document.getElementById('typePill').textContent = '題型';
    document.getElementById('sourcePill').textContent = '來源';
    return;
  }}
  const q = session[current];
  const saved = answerFor(q);
  const shouldReveal = submitted || Boolean(saved);
  document.getElementById('typePill').textContent = q.autoGradable ? TYPE_LABELS[q.type] || q.type : '自我核對';
  document.getElementById('sourcePill').textContent = `${{q.source}} #${{q.sourceIndex}}`;
  area.innerHTML = renderQuestion(q, saved, shouldReveal);
  bindQuestionEvents(q);
}}
function renderQuestion(q, saved, reveal) {{
  const category = q.categories.map(id => OUTLINE_LABELS[id] || id).join(' / ') || '未分類';
  const selected = saved?.selected || [];
  const optionsHtml = q.autoGradable ? `<div class="options">${{q.options.map(opt => {{
    const checked = selected.includes(opt.value) ? 'checked' : '';
    const isCorrect = reveal && q.correctValues.includes(opt.value);
    const isWrong = reveal && selected.includes(opt.value) && !q.correctValues.includes(opt.value);
    const className = isCorrect ? 'correct' : (isWrong ? 'wrong' : '');
    const inputType = q.type === 'multiple' ? 'checkbox' : 'radio';
    return `<label class="option ${{className}}"><input type="${{inputType}}" name="answer" value="${{escapeAttr(opt.value)}}" ${{checked}} ${{reveal ? 'disabled' : ''}}><span>${{opt.html}}</span></label>`;
  }}).join('')}}</div>` : `<div class="question-body">${{q.fullQuestionHtml}}</div>`;
  const feedback = saved ? feedbackHtml(q, saved) : '';
  const answerClass = reveal ? 'answer-panel show' : 'answer-panel';
  const favoriteActive = state.favorites[q.id] ? 'active' : '';
  return `<article class="question-card">
    <div class="question-head">
      <div>
        <h3 class="question-title">#${{q.number}} ${{escapeHtml(q.title)}}</h3>
        <div class="question-meta">${{escapeHtml(category)}}<br>${{escapeHtml(q.meta)}}</div>
      </div>
      <span class="pill">${{q.autoGradable ? '自動判分' : '自我核對'}}</span>
    </div>
    <div class="question-body">
      ${{q.stemHtml}}
      ${{optionsHtml}}
      ${{feedback}}
      <div class="${{answerClass}}" id="answerPanel">${{q.answerHtml}}</div>
    </div>
    <div class="card-actions">
      <div class="button-row">
        <button class="btn" id="prevBtn">上一題</button>
        <button class="btn" id="nextBtn">下一題</button>
        <button class="btn ghost ${{favoriteActive}}" id="favBtn">${{state.favorites[q.id] ? '已收藏' : '收藏'}}</button>
      </div>
      <div class="button-row">
        <button class="btn" id="revealBtn">${{reveal ? '隱藏解析' : '顯示解析'}}</button>
        <button class="btn primary" id="submitBtn">${{q.autoGradable ? '送出答案' : '標記已練習'}}</button>
      </div>
    </div>
  </article>`;
}}
function feedbackHtml(q, saved) {{
  if (!q.autoGradable) return '<div class="feedback review show">此題已標記練習，請依解析自我核對。</div>';
  return saved.correct
    ? '<div class="feedback correct show">答對了。解析已展開，考前可快速掃過重點。</div>'
    : `<div class="feedback wrong show">答錯了。正確答案：${{q.correctValues.join(', ')}}</div>`;
}}
function bindQuestionEvents(q) {{
  document.getElementById('prevBtn').addEventListener('click', () => {{ current = Math.max(0, current - 1); submitted = false; render(); }});
  document.getElementById('nextBtn').addEventListener('click', () => {{ current = Math.min(session.length - 1, current + 1); submitted = false; render(); }});
  document.getElementById('favBtn').addEventListener('click', () => {{
    if (state.favorites[q.id]) delete state.favorites[q.id]; else state.favorites[q.id] = true;
    saveState(); render();
  }});
  document.getElementById('revealBtn').addEventListener('click', () => {{
    submitted = !document.getElementById('answerPanel').classList.contains('show');
    render();
  }});
  document.getElementById('submitBtn').addEventListener('click', () => submitAnswer(q));
}}
function submitAnswer(q) {{
  let selected = [];
  if (q.autoGradable) selected = [...document.querySelectorAll('input[name="answer"]:checked')].map(input => input.value);
  const correct = q.autoGradable ? sameSet(selected, q.correctValues) : null;
  state.answers[q.id] = {{ selected, correct, autoGradable: q.autoGradable, at: new Date().toISOString() }};
  submitted = true;
  saveState();
  render();
}}
function escapeHtml(value) {{
  return String(value || '').replace(/[&<>"']/g, char => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[char]));
}}
function escapeAttr(value) {{ return escapeHtml(value); }}
function tickCountdown() {{
  const diff = EXAM_TIME - new Date();
  const el = document.getElementById('countdown');
  if (diff <= 0) {{ el.textContent = '考試時間已到：2026/06/30 16:45'; return; }}
  const totalMinutes = Math.floor(diff / 60000);
  const days = Math.floor(totalMinutes / 1440);
  const hours = Math.floor((totalMinutes % 1440) / 60);
  const minutes = totalMinutes % 60;
  el.textContent = `距離 2026/06/30 16:45 還有 ${{days}} 天 ${{hours}} 小時 ${{minutes}} 分`;
}}
document.getElementById('shuffleBtn').addEventListener('click', () => newSession());
document.getElementById('resetBtn').addEventListener('click', () => {{
  if (!confirm('確定清除本機答題紀錄、錯題與收藏？')) return;
  state = {{ answers: {{}}, favorites: {{}}, seed: Date.now() }};
  saveState();
  newSession();
}});
renderControls();
newSession();
tickCountdown();
setInterval(tickCountdown, 30000);
</script>
</body>
</html>
"""


def main() -> None:
    questions = build_questions()
    counts = {source: 0 for source, _, _ in SOURCES}
    auto = 0
    for q in questions:
        counts[q["id"].split("-", 1)[0]] += 1
        auto += int(q["autoGradable"])
    if len(questions) != 475:
        raise SystemExit(f"Expected 475 questions, got {len(questions)}")
    html = build_html(questions)
    (ROOT / "ai900_quiz_machine.html").write_text(html, encoding="utf-8")
    print(f"Generated ai900_quiz_machine.html with {len(questions)} questions ({auto} auto-gradable)")
    print(counts)


if __name__ == "__main__":
    main()
