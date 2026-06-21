#!/usr/bin/env python3
"""Production infographic renderer for The Batch 358.

The image model is used for the visual direction; all text, numbers, charts,
and geometry are rendered deterministically here so Traditional Chinese and
benchmark values remain exact.
"""

from __future__ import annotations

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).parent / "images"
OUT.mkdir(exist_ok=True)

FONT_REGULAR = "/System/Library/Fonts/STHeiti Light.ttc"
FONT_BOLD = "/System/Library/Fonts/STHeiti Medium.ttc"

NAVY = "#071521"
NAVY_2 = "#0D2234"
CARD = "#102B40"
CARD_2 = "#14364E"
WHITE = "#F7FAFC"
MUTED = "#A9BBC8"
CYAN = "#35C5D5"
BLUE = "#4EA5FF"
ORANGE = "#FF8A3D"
RED = "#FF5D5D"
GREEN = "#4BD29B"
PURPLE = "#A786FF"
YELLOW = "#F7C948"
GRID = "#24465C"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REGULAR, size)


def gradient(size: tuple[int, int], top=NAVY, bottom="#0B2638") -> Image.Image:
    w, h = size
    a = tuple(int(top[i : i + 2], 16) for i in (1, 3, 5))
    b = tuple(int(bottom[i : i + 2], 16) for i in (1, 3, 5))
    im = Image.new("RGB", size)
    px = im.load()
    for y in range(h):
        t = y / max(h - 1, 1)
        color = tuple(round(a[i] * (1 - t) + b[i] * t) for i in range(3))
        for x in range(w):
            px[x, y] = color
    return im


def base(size: tuple[int, int]) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    im = gradient(size)
    d = ImageDraw.Draw(im)
    w, h = size
    step = max(56, w // 24)
    for x in range(0, w, step):
        d.line((x, 0, x, h), fill=GRID, width=1)
    for y in range(0, h, step):
        d.line((0, y, w, y), fill=GRID, width=1)
    d.ellipse((-w * .15, -h * .25, w * .42, h * .4), fill="#0D3146")
    d.ellipse((w * .72, h * .67, w * 1.15, h * 1.16), fill="#12324A")
    return im, d


def rr(d, box, radius=28, fill=CARD, outline=None, width=2):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text(d, xy, value, size, fill=WHITE, bold=False, anchor="la"):
    d.text(xy, value, font=font(size, bold), fill=fill, anchor=anchor)


def fit_lines(value: str, max_chars: int) -> list[str]:
    lines = []
    for raw in value.split("\n"):
        if not raw:
            lines.append("")
        elif len(raw) <= max_chars:
            lines.append(raw)
        else:
            lines.extend(wrap(raw, max_chars, break_long_words=False, break_on_hyphens=False))
    return lines


def paragraph(d, box, value, size, fill=MUTED, bold=False, spacing=1.36, max_chars=None):
    x1, y1, x2, _ = box
    if max_chars is None:
        max_chars = max(8, int((x2 - x1) / (size * .95)))
    y = y1
    for line in fit_lines(value, max_chars):
        d.text((x1, y), line, font=font(size, bold), fill=fill)
        y += int(size * spacing)
    return y


def header(d, w, title, subtitle, mobile=False, accent=CYAN):
    pad = 68 if mobile else 86
    top = 82 if mobile else 54
    text(d, (pad, top), "THE BATCH 358  /  DEEP GUIDE", 22 if mobile else 17, accent, True)
    paragraph(
        d,
        (pad, top + (58 if mobile else 42), w - pad, 350),
        title,
        58 if mobile else 48,
        WHITE,
        True,
        1.18,
        15 if mobile else 29,
    )
    paragraph(
        d,
        (pad, top + (210 if mobile else 112), w - pad, 390),
        subtitle,
        27 if mobile else 23,
        MUTED,
        False,
        1.3,
        31 if mobile else 65,
    )


def footer(d, w, h, label):
    d.line((64, h - 62, w - 64, h - 62), fill=GRID, width=2)
    text(d, (64, h - 34), label, 16, MUTED, anchor="lm")
    text(d, (w - 64, h - 34), "AI SUPPLY-CHAIN SOVEREIGNTY", 16, CYAN, True, anchor="rm")


def save(im, name):
    path = OUT / name
    im.save(path, "PNG", optimize=True, dpi=(300, 300))
    print(f"✓ {path.name}  {im.width}×{im.height}")


def card_title(d, x, y, index, label, color, mobile=False):
    r = 31 if mobile else 24
    d.ellipse((x, y, x + r * 2, y + r * 2), fill=color)
    text(d, (x + r, y + r + 1), str(index), 26 if mobile else 20, NAVY, True, "mm")
    text(d, (x + r * 2 + 20, y + r), label, 31 if mobile else 25, WHITE, True, "lm")


def infographic_0(mobile=False):
    size = (1080, 1920) if mobile else (1920, 1080)
    im, d = base(size)
    w, h = size
    header(d, w, "AI 供應鏈危機四步演進流", "從競爭限制、隱形降級到主權 AI 覺醒", mobile, ORANGE)
    events = [
        ("2025 / 04", "競爭限制", "Fable 5 加入競品開發限制", "開發者質疑 vendor lock-in", BLUE),
        ("T + 1 週", "隱形降級", "Claude Code 模式暗中降級", "信任、稽核與合規風險", ORANGE),
        ("T + 3 週", "出口管制", "存取限制升高為地緣衝擊", "全球 AI 供應鏈震盪", RED),
        ("T + 4 週", "主權覺醒", "轉向開源與在地基礎設施", "DeepSeek／Qwen／Kimi 加速", GREEN),
    ]
    if mobile:
        y = 405
        for i, (date, name, desc, impact, color) in enumerate(events, 1):
            rr(d, (62, y, w - 62, y + 285), 32, CARD, color, 3)
            card_title(d, 96, y + 32, i, name, color, True)
            text(d, (w - 96, y + 64), date, 24, color, True, "rm")
            paragraph(d, (96, y + 122, w - 96, y + 205), desc, 28, WHITE, True, max_chars=29)
            paragraph(d, (96, y + 205, w - 96, y + 270), "全球反應｜" + impact, 24, MUTED, max_chars=33)
            if i < 4:
                d.line((w // 2, y + 286, w // 2, y + 330), fill=color, width=5)
                d.polygon(((w // 2 - 12, y + 320), (w // 2 + 12, y + 320), (w // 2, y + 338)), fill=color)
            y += 330
        rr(d, (62, 1735, w - 62, 1832), 28, "#16364B")
        text(d, (w // 2, 1784), "開源 AI 投資 ↑40%　｜　進口限制 ↑25%", 27, YELLOW, True, "mm")
    else:
        y1, y2 = 330, 790
        gap, margin = 28, 74
        cw = (w - margin * 2 - gap * 3) // 4
        for i, (date, name, desc, impact, color) in enumerate(events, 1):
            x = margin + (i - 1) * (cw + gap)
            rr(d, (x, y1, x + cw, y2), 28, CARD, color, 3)
            card_title(d, x + 30, y1 + 30, i, name, color)
            text(d, (x + 30, y1 + 112), date, 22, color, True)
            paragraph(d, (x + 30, y1 + 165, x + cw - 30, y1 + 265), desc, 26, WHITE, True, max_chars=16)
            d.line((x + 30, y1 + 290, x + cw - 30, y1 + 290), fill=GRID, width=2)
            text(d, (x + 30, y1 + 324), "全球反應", 18, MUTED, True)
            paragraph(d, (x + 30, y1 + 362, x + cw - 30, y2 - 20), impact, 22, WHITE, max_chars=16)
            if i < 4:
                ax = x + cw + 5
                d.line((ax, (y1 + y2) // 2, ax + gap - 10, (y1 + y2) // 2), fill=color, width=5)
        rr(d, (410, 845, 1510, 945), 30, "#16364B")
        text(d, (960, 895), "開源 AI 投資 ↑40%　｜　進口限制 ↑25%", 30, YELLOW, True, "mm")
    footer(d, w, h, "圖 0｜危機升級路徑")
    save(im, "infographic_0_supply_chain_escalation-mobile.png" if mobile else "infographic_0_supply_chain_escalation.png")


def infographic_1(mobile=False):
    size = (1080, 1920) if mobile else (1920, 1080)
    im, d = base(size)
    w, h = size
    header(d, w, "Fable 5 隱形降級風波", "從廠商控制到市場衝擊的 4 週", mobile, RED)
    events = [
        ("T0", "限制條款上線", "禁止用於競品 LLM 開發", "中度", YELLOW),
        ("T+1w", "偵測到隱形降級", "Claude Code 未通知切換能力", "高", ORANGE),
        ("T+2w", "輿論反彈", "改為透明通知，但仍限制能力", "中高", ORANGE),
        ("T+3w", "出口管制衝擊", "模型存取成為地緣政治工具", "嚴重", RED),
        ("T+4w", "全球供應鏈震盪", "企業與國家轉向替代方案", "嚴重", RED),
    ]
    if mobile:
        line_x, y0, step = 112, 430, 270
        d.line((line_x, y0, line_x, y0 + step * 4), fill=GRID, width=8)
        for i, (week, name, desc, sev, color) in enumerate(events):
            y = y0 + i * step
            d.ellipse((line_x - 24, y - 24, line_x + 24, y + 24), fill=color)
            rr(d, (168, y - 78, w - 58, y + 150), 28, CARD, color, 3)
            text(d, (202, y - 42), week, 23, color, True)
            text(d, (w - 92, y - 42), "風險｜" + sev, 21, color, True, "ra")
            paragraph(d, (202, y + 8, w - 94, y + 70), name, 30, WHITE, True, max_chars=20)
            paragraph(d, (202, y + 70, w - 94, y + 138), desc, 23, MUTED, max_chars=29)
        rr(d, (58, 1710, w - 58, 1815), 26, "#351D29", RED, 2)
        text(d, (w // 2, 1762), "4 週內：信任問題 → 供應鏈問題", 28, WHITE, True, "mm")
    else:
        xline, top, step = 960, 310, 135
        d.line((xline, top, xline, top + step * 4), fill=GRID, width=8)
        for i, (week, name, desc, sev, color) in enumerate(events):
            y = top + i * step
            left = i % 2 == 0
            d.ellipse((xline - 20, y - 20, xline + 20, y + 20), fill=color)
            box = (130, y - 55, 875, y + 78) if left else (1045, y - 55, 1790, y + 78)
            rr(d, box, 24, CARD, color, 3)
            tx = box[0] + 28
            text(d, (tx, y - 29), week + "　" + name, 25, WHITE, True)
            paragraph(d, (tx, y + 15, box[2] - 145, y + 72), desc, 20, MUTED, max_chars=30)
            text(d, (box[2] - 26, y + 15), sev, 20, color, True, "rm")
            d.line((box[2] if left else box[0], y, xline, y), fill=color, width=3)
        text(d, (960, 905), "從服務條款一路升高為全球市場衝擊", 27, YELLOW, True, "mm")
    footer(d, w, h, "圖 1｜事件時間線")
    save(im, "infographic_1_fable_timeline-mobile.png" if mobile else "infographic_1_fable_timeline.png")


def infographic_2(mobile=False):
    size = (1080, 1920) if mobile else (1920, 1080)
    im, d = base(size)
    w, h = size
    header(d, w, "AI Agent 評測邊界轉移", "從 bug 修補，走向完整程式與系統故障診斷", mobile, BLUE)
    items = [
        ("SWE-bench", "Bug fixes", "★★☆☆☆", "~100 行", "90%+｜已飽和", MUTED),
        ("DeepSWE", "Feature implementation", "★★★★☆", "約 550 行", "GPT-5.5｜70%", BLUE),
        ("ProgramBench", "End-to-end synthesis", "★★★★★", "完整可執行程式", "Claude Opus 4.7｜3%", ORANGE),
        ("ITBench-AA", "Root cause analysis", "★★★★★", "59 起真實事故", "Claude Opus 4.7｜46.7%", GREEN),
    ]
    if mobile:
        y = 410
        for name, kind, stars, scope, score, color in items:
            rr(d, (58, y, w - 58, y + 295), 30, CARD, color, 3)
            text(d, (92, y + 46), name, 34, WHITE, True)
            text(d, (w - 92, y + 49), stars, 25, color, True, "ra")
            text(d, (92, y + 104), kind, 23, color, True)
            d.line((92, y + 148, w - 92, y + 148), fill=GRID, width=2)
            text(d, (92, y + 188), "工作範圍", 20, MUTED, True)
            text(d, (w - 92, y + 188), scope, 23, WHITE, True, "ra")
            text(d, (92, y + 242), "代表成績", 20, MUTED, True)
            text(d, (w - 92, y + 242), score, 23, color, True, "ra")
            y += 320
        rr(d, (58, 1730, w - 58, 1828), 26, "#16364B")
        text(d, (w // 2, 1779), "能力邊界：Coding → Systems Thinking", 27, CYAN, True, "mm")
    else:
        margin, gap, y1, y2 = 64, 24, 330, 810
        cw = (w - margin * 2 - gap * 3) // 4
        for i, (name, kind, stars, scope, score, color) in enumerate(items):
            x = margin + i * (cw + gap)
            rr(d, (x, y1, x + cw, y2), 28, CARD if i else "#172A37", color, 3)
            text(d, (x + 28, y1 + 44), "LEGACY" if i == 0 else f"NEXT GEN 0{i}", 17, color, True)
            paragraph(d, (x + 28, y1 + 92, x + cw - 28, y1 + 155), name, 30, WHITE, True, max_chars=19)
            paragraph(d, (x + 28, y1 + 158, x + cw - 28, y1 + 230), kind, 21, color, True, max_chars=22)
            text(d, (x + 28, y1 + 264), stars, 23, color, True)
            d.line((x + 28, y1 + 310, x + cw - 28, y1 + 310), fill=GRID, width=2)
            text(d, (x + 28, y1 + 348), scope, 22, WHITE, True)
            paragraph(d, (x + 28, y1 + 400, x + cw - 28, y2 - 20), score, 22, MUTED, max_chars=22)
        text(d, (960, 895), "能力邊界從「寫程式」轉向「理解並修復系統」", 29, CYAN, True, "mm")
    footer(d, w, h, "圖 2｜Benchmark evolution")
    save(im, "infographic_2_benchmark_evolution-mobile.png" if mobile else "infographic_2_benchmark_evolution.png")


def infographic_3(mobile=False):
    size = (1080, 1920) if mobile else (1920, 1080)
    im, d = base(size)
    w, h = size
    header(d, w, "Nemotron 3 Ultra 550B", "混合 Transformer–Mamba MoE 與多師蒸餾管道", mobile, PURPLE)
    specs = [("550B", "總參數"), ("55B", "每 token 啟用"), ("183", "tokens / sec"), ("1M", "context")]
    if mobile:
        for i, (v, k) in enumerate(specs):
            x = 58 + (i % 2) * 493
            y = 405 + (i // 2) * 145
            rr(d, (x, y, x + 465, y + 120), 24, CARD_2)
            text(d, (x + 28, y + 38), v, 38, CYAN, True)
            text(d, (x + 28, y + 87), k, 20, MUTED)
        y = 720
        blocks = [("MAMBA", "長序列低記憶體", BLUE), ("SELF-ATTENTION", "精準 token recall", PURPLE), ("LATENT MoE", "路由至 10 位專家", ORANGE)]
        for name, desc, color in blocks:
            rr(d, (116, y, w - 116, y + 180), 30, CARD, color, 3)
            text(d, (w // 2, y + 62), name, 30, color, True, "mm")
            text(d, (w // 2, y + 120), desc, 24, WHITE, True, "mm")
            y += 220
        rr(d, (58, 1400, w - 58, 1790), 30, "#102A3D")
        text(d, (92, 1450), "TRAINING PIPELINE", 23, GREEN, True)
        stages = [("01", "20T tokens 預訓練"), ("02", "SFT + RL｜6 domains"), ("03", "10+ 多師蒸餾｜2 rounds")]
        yy = 1525
        for n, label in stages:
            text(d, (102, yy), n, 25, GREEN, True)
            text(d, (180, yy), label, 27, WHITE, True)
            yy += 85
    else:
        y = 290
        for i, (v, k) in enumerate(specs):
            x = 85 + i * 445
            rr(d, (x, y, x + 405, y + 112), 24, CARD_2)
            text(d, (x + 28, y + 34), v, 36, CYAN, True)
            text(d, (x + 28, y + 82), k, 18, MUTED)
        blocks = [("MAMBA", "長序列低記憶體", BLUE), ("SELF-ATTENTION", "精準 token recall", PURPLE), ("LATENT MoE", "壓縮並路由至 10 位專家", ORANGE)]
        bx, by, bw = 150, 475, 480
        for i, (name, desc, color) in enumerate(blocks):
            x = bx + i * 570
            rr(d, (x, by, x + bw, by + 205), 30, CARD, color, 3)
            text(d, (x + bw // 2, by + 70), name, 27, color, True, "mm")
            text(d, (x + bw // 2, by + 136), desc, 21, WHITE, True, "mm")
            if i < 2:
                d.line((x + bw + 20, by + 102, x + 550, by + 102), fill=CYAN, width=5)
                d.polygon(((x + 540, by + 90), (x + 560, by + 102), (x + 540, by + 114)), fill=CYAN)
        rr(d, (150, 735, 1770, 925), 30, "#102A3D")
        stages = [("01", "20T tokens\n預訓練"), ("02", "SFT + RL\n6 domains"), ("03", "10+ teachers\n多師蒸餾"), ("RESULT", "47.7%\nIntelligence Index")]
        for i, (n, label) in enumerate(stages):
            x = 190 + i * 390
            text(d, (x, 785), n, 19, GREEN if i < 3 else YELLOW, True)
            paragraph(d, (x, 825, x + 310, 910), label, 23, WHITE, True, max_chars=18)
    footer(d, w, h, "圖 3｜Architecture & training")
    save(im, "infographic_3_nemotron_architecture-mobile.png" if mobile else "infographic_3_nemotron_architecture.png")


def infographic_4(mobile=False):
    size = (1080, 1920) if mobile else (1920, 1080)
    im, d = base(size)
    w, h = size
    header(d, w, "供應鏈限制的歷史回音", "一旦存取受威脅，市場就會加速打造替代方案", mobile, ORANGE)
    stages = [
        ("2018–2022", "半導體", "出口管制先進晶片", "中國研發投資 ↑300%", "自主製造加速", BLUE),
        ("2010–2020", "稀土", "對日出口限制", "替代礦源投資 ↑50%", "集中度 95% → 60%", GREEN),
        ("2025–NOW", "AI 模型", "前沿模型存取限制", "開源資金 ↑40–60% YoY", "主權 AI 全面啟動", ORANGE),
    ]
    if mobile:
        y = 420
        for period, name, trigger, invest, result, color in stages:
            rr(d, (58, y, w - 58, y + 380), 32, CARD, color, 3)
            text(d, (92, y + 50), period, 23, color, True)
            text(d, (w - 92, y + 50), name, 37, WHITE, True, "ra")
            paragraph(d, (92, y + 120, w - 92, y + 190), "觸發｜" + trigger, 25, MUTED, max_chars=29)
            paragraph(d, (92, y + 205, w - 92, y + 275), "投資｜" + invest, 27, color, True, max_chars=28)
            paragraph(d, (92, y + 292, w - 92, y + 355), "結果｜" + result, 25, WHITE, max_chars=29)
            y += 415
        rr(d, (58, 1695, w - 58, 1825), 30, "#3A291A", ORANGE, 2)
        paragraph(d, (90, 1725, w - 90, 1810), "限制原本想降低能力擴散，卻往往加速替代生態成熟。", 26, WHITE, True, max_chars=28)
    else:
        margin, gap, y1, y2 = 76, 34, 330, 820
        cw = (w - margin * 2 - gap * 2) // 3
        for i, (period, name, trigger, invest, result, color) in enumerate(stages):
            x = margin + i * (cw + gap)
            rr(d, (x, y1, x + cw, y2), 30, CARD, color, 3)
            text(d, (x + 32, y1 + 50), period, 21, color, True)
            text(d, (x + 32, y1 + 110), name, 38, WHITE, True)
            d.line((x + 32, y1 + 170, x + cw - 32, y1 + 170), fill=GRID, width=2)
            paragraph(d, (x + 32, y1 + 205, x + cw - 32, y1 + 280), "觸發｜" + trigger, 23, MUTED, max_chars=23)
            paragraph(d, (x + 32, y1 + 310, x + cw - 32, y1 + 390), invest, 29, color, True, max_chars=20)
            paragraph(d, (x + 32, y1 + 420, x + cw - 32, y2 - 20), result, 23, WHITE, max_chars=23)
        text(d, (960, 900), "限制存取 → 投資替代 → 供應鏈重組", 31, YELLOW, True, "mm")
    footer(d, w, h, "圖 4｜Geopolitical pattern")
    save(im, "infographic_4_geopolitical_supply_chain-mobile.png" if mobile else "infographic_4_geopolitical_supply_chain.png")


def infographic_5(mobile=False):
    size = (1080, 1920) if mobile else (1920, 1080)
    im, d = base(size)
    w, h = size
    header(d, w, "POPE：把難題拆成可學習路徑", "Privileged On-Policy Exploration 的四階段訓練流程", mobile, GREEN)
    phases = [
        ("01", "問題篩選", "基線失敗 128+ 次\n鎖定真正難題", BLUE),
        ("02", "前綴提取", "找出能啟動解題的\n最小提示", PURPLE),
        ("03", "GRPO 雙軌訓練", "50% 有提示\n50% 無提示", ORANGE),
        ("04", "漸進移除提示", "先學會完成\n再學會從零開始", GREEN),
    ]
    if mobile:
        y = 410
        for i, (num, name, desc, color) in enumerate(phases):
            rr(d, (58, y, w - 58, y + 250), 30, CARD, color, 3)
            text(d, (100, y + 58), num, 30, color, True)
            text(d, (190, y + 58), name, 32, WHITE, True)
            paragraph(d, (100, y + 122, w - 90, y + 230), desc, 25, MUTED, max_chars=29)
            if i < 3:
                d.line((w // 2, y + 250, w // 2, y + 292), fill=color, width=5)
            y += 292
        rr(d, (58, 1610, w - 58, 1820), 28, "#11382E", GREEN, 2)
        text(d, (92, 1660), "核心教學洞察", 24, GREEN, True)
        paragraph(d, (92, 1710, w - 92, 1800), "先從已知中點學會完成，再撤除鷹架，學會自行找到起點。", 27, WHITE, True, max_chars=29)
    else:
        margin, gap, y1, y2 = 66, 30, 330, 690
        cw = (w - margin * 2 - gap * 3) // 4
        for i, (num, name, desc, color) in enumerate(phases):
            x = margin + i * (cw + gap)
            rr(d, (x, y1, x + cw, y2), 28, CARD, color, 3)
            text(d, (x + 30, y1 + 54), num, 28, color, True)
            paragraph(d, (x + 30, y1 + 110, x + cw - 30, y1 + 180), name, 29, WHITE, True, max_chars=15)
            d.line((x + 30, y1 + 205, x + cw - 30, y1 + 205), fill=GRID, width=2)
            paragraph(d, (x + 30, y1 + 240, x + cw - 30, y2 - 20), desc, 23, MUTED, max_chars=17)
            if i < 3:
                d.line((x + cw + 5, (y1 + y2) // 2, x + cw + gap - 5, (y1 + y2) // 2), fill=color, width=5)
        rr(d, (150, 750, 1770, 925), 30, "#11382E", GREEN, 2)
        text(d, (205, 805), "LEARNING PRINCIPLE", 20, GREEN, True)
        text(d, (205, 862), "先學會「從中點完成」 → 再學會「從起點獨立解題」", 31, WHITE, True)
    footer(d, w, h, "圖 5｜POPE training flow")
    save(im, "infographic_5_pope_training_flow-mobile.png" if mobile else "infographic_5_pope_training_flow.png")


def bars(d, box, rows, max_value, mobile=False):
    x1, y1, x2, y2 = box
    row_h = (y2 - y1) / len(rows)
    label_w = 200 if mobile else 180
    for i, (label, value, color) in enumerate(rows):
        y = y1 + i * row_h
        text(d, (x1, y + row_h * .48), label, 21 if mobile else 18, WHITE, True, "lm")
        bx = x1 + label_w
        bw = x2 - bx - 95
        rr(d, (bx, y + row_h * .24, bx + bw, y + row_h * .7), 16, "#18384D")
        fill_w = bw * value / max_value
        rr(d, (bx, y + row_h * .24, bx + fill_w, y + row_h * .7), 16, color)
        text(d, (x2, y + row_h * .48), f"{value:g}%", 20 if mobile else 18, color, True, "rm")


def infographic_6(mobile=False):
    size = (1080, 1920) if mobile else (1920, 1080)
    im, d = base(size)
    w, h = size
    header(d, w, "POPE vs GRPO：單次機會最有價值", "優勢集中在 pass@1；重試次數增加後差距縮小", mobile, BLUE)
    aime1 = [("SFT", 30, MUTED), ("GRPO", 49.6, ORANGE), ("POPE", 53.1, BLUE)]
    aime16 = [("SFT", 40, MUTED), ("GRPO", 81.4, ORANGE), ("POPE", 82.6, BLUE)]
    hmmt1 = [("GRPO", 31, ORANGE), ("POPE", 37.8, BLUE)]
    hmmt16 = [("GRPO", 63.8, ORANGE), ("POPE", 67.5, BLUE)]
    groups = [("AIME 2025｜pass@1", aime1, 90), ("AIME 2025｜pass@16", aime16, 90),
              ("HMMT 2025｜pass@1", hmmt1, 75), ("HMMT 2025｜pass@16", hmmt16, 75)]
    if mobile:
        y = 405
        for title_, rows, maxv in groups:
            rr(d, (58, y, w - 58, y + 295), 28, CARD)
            text(d, (92, y + 42), title_, 27, WHITE, True)
            bars(d, (92, y + 88, w - 92, y + 270), rows, maxv, True)
            y += 320
        rr(d, (58, 1708, w - 58, 1825), 28, "#16364B", BLUE, 2)
        text(d, (w // 2, 1766), "適合：低延遲、低 token、一次決策", 27, CYAN, True, "mm")
    else:
        positions = [(74, 330, 920, 605), (1000, 330, 1846, 605), (74, 650, 920, 925), (1000, 650, 1846, 925)]
        for (title_, rows, maxv), box in zip(groups, positions):
            rr(d, box, 28, CARD)
            text(d, (box[0] + 32, box[1] + 42), title_, 25, WHITE, True)
            bars(d, (box[0] + 32, box[1] + 78, box[2] - 32, box[3] - 24), rows, maxv)
        text(d, (960, 970), "pass@1：AIME +3.5pp｜HMMT +6.8pp", 24, CYAN, True, "mm")
    footer(d, w, h, "圖 6｜Performance comparison")
    save(im, "infographic_6_pope_performance_comparison-mobile.png" if mobile else "infographic_6_pope_performance_comparison.png")


def fable_mechanism(mobile=False):
    size = (1080, 1920) if mobile else (1920, 1080)
    im, d = base(size)
    w, h = size
    header(d, w, "Fable 5 黑盒防禦機制", "同一個敏感提示，在不同入口產生不同處置與稽核風險", mobile, RED)
    nodes = [
        ("USER PROMPT", "使用者請求", BLUE),
        ("CLASSIFIER", "敏感意圖分類器", ORANGE),
        ("API MODE", "直接拒絕 Refusal", RED),
        ("TOOL MODE", "暗中路由至 Opus 4.8", PURPLE),
        ("AUDIT RISK", "輸出未標示切換；僅留在額外日誌", YELLOW),
    ]
    if mobile:
        boxes = [
            (120, 420, 960, 600),
            (120, 700, 960, 880),
            (58, 1000, 505, 1235),
            (575, 1000, 1022, 1235),
            (120, 1410, 960, 1660),
        ]
        for (label, desc, color), box in zip(nodes, boxes):
            rr(d, box, 30, CARD, color, 3)
            text(d, ((box[0] + box[2]) // 2, box[1] + 60), label, 27, color, True, "mm")
            paragraph(d, (box[0] + 34, box[1] + 105, box[2] - 34, box[3] - 20), desc, 25, WHITE, True, max_chars=25)
        d.line((540, 600, 540, 700), fill=CYAN, width=6)
        d.line((540, 880, 540, 940), fill=ORANGE, width=6)
        d.line((282, 940, 798, 940), fill=ORANGE, width=6)
        d.line((282, 940, 282, 1000), fill=RED, width=6)
        d.line((798, 940, 798, 1000), fill=PURPLE, width=6)
        d.line((798, 1235, 798, 1340), fill=YELLOW, width=6)
        d.line((540, 1340, 798, 1340), fill=YELLOW, width=6)
        d.line((540, 1340, 540, 1410), fill=YELLOW, width=6)
        rr(d, (58, 1715, w - 58, 1825), 28, "#3A2D17", YELLOW, 2)
        text(d, (w // 2, 1770), "不可觀測的模型切換 = 合規證據鏈斷裂", 27, WHITE, True, "mm")
    else:
        boxes = [
            (70, 440, 365, 650),
            (455, 440, 790, 650),
            (920, 300, 1320, 500),
            (920, 600, 1320, 800),
            (1450, 440, 1840, 650),
        ]
        for (label, desc, color), box in zip(nodes, boxes):
            rr(d, box, 28, CARD, color, 3)
            text(d, ((box[0] + box[2]) // 2, box[1] + 62), label, 24, color, True, "mm")
            paragraph(d, (box[0] + 28, box[1] + 112, box[2] - 28, box[3] - 20), desc, 22, WHITE, True, max_chars=20)
        d.line((365, 545, 455, 545), fill=CYAN, width=6)
        d.line((790, 545, 850, 545), fill=ORANGE, width=6)
        d.line((850, 400, 850, 700), fill=ORANGE, width=6)
        d.line((850, 400, 920, 400), fill=RED, width=6)
        d.line((850, 700, 920, 700), fill=PURPLE, width=6)
        d.line((1320, 700, 1390, 700), fill=YELLOW, width=6)
        d.line((1390, 545, 1390, 700), fill=YELLOW, width=6)
        d.line((1390, 545, 1450, 545), fill=YELLOW, width=6)
        rr(d, (450, 860, 1470, 950), 26, "#3A2D17", YELLOW, 2)
        text(d, (960, 905), "不可觀測的模型切換 = 合規證據鏈斷裂", 28, WHITE, True, "mm")
    footer(d, w, h, "機制圖｜Routing & auditability")
    save(im, "fable_mechanism-mobile.png" if mobile else "fable_mechanism.png")


def summary_visual(mobile=False):
    size = (1080, 1920) if mobile else (1920, 1080)
    im, d = base(size)
    w, h = size
    header(d, w, "掌控權的幽靈", "AI 時代的供應鏈主權與防禦邊界｜一圖掌握全文", mobile, CYAN)
    chapters = [
        ("01", "數位水電被收回", "單一模型 API 是營運集中風險", BLUE),
        ("02", "黑盒防禦死角", "隱形降級破壞可觀測性與稽核", RED),
        ("03", "評測邊界升級", "從 coding 走向 SysOps 與事故診斷", PURPLE),
        ("04", "主權 AI 覺醒", "限制存取反而加速開源替代", ORANGE),
        ("05", "POPE 訓練路徑", "先給鷹架，再逐步移除提示", GREEN),
    ]
    if mobile:
        y = 405
        for num, name, desc, color in chapters:
            rr(d, (58, y, w - 58, y + 235), 30, CARD, color, 3)
            text(d, (92, y + 56), num, 28, color, True)
            text(d, (185, y + 56), name, 31, WHITE, True)
            paragraph(d, (92, y + 125, w - 92, y + 215), desc, 25, MUTED, max_chars=29)
            y += 260
        rr(d, (58, 1720, w - 58, 1825), 28, "#16364B")
        text(d, (w // 2, 1772), "核心原則｜韌性優先、可觀測、可替代", 27, YELLOW, True, "mm")
    else:
        top = [(70, 335, 620, 585), (685, 335, 1235, 585), (1300, 335, 1850, 585)]
        bottom = [(375, 650, 925, 900), (995, 650, 1545, 900)]
        for (num, name, desc, color), box in zip(chapters, top + bottom):
            rr(d, box, 30, CARD, color, 3)
            text(d, (box[0] + 30, box[1] + 48), num, 25, color, True)
            text(d, (box[0] + 100, box[1] + 48), name, 29, WHITE, True)
            paragraph(d, (box[0] + 30, box[1] + 115, box[2] - 30, box[3] - 20), desc, 23, MUTED, max_chars=24)
        text(d, (960, 965), "韌性優先　｜　可觀測　｜　可替代", 28, YELLOW, True, "mm")
    footer(d, w, h, "SUMMARY｜The Batch Issue 358")
    save(im, "summary-mobile.png" if mobile else "summary.png")


def main():
    for fn in (
        infographic_0,
        infographic_1,
        infographic_2,
        infographic_3,
        infographic_4,
        infographic_5,
        infographic_6,
    ):
        fn(False)
        fn(True)
    fable_mechanism(False)
    fable_mechanism(True)
    summary_visual(False)
    summary_visual(True)


if __name__ == "__main__":
    main()
