#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成 7 個複雜信息圖表：AI 供應鏈危機分析
支援傳統中文、16:9 比例、300 DPI
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from datetime import datetime, timedelta
import os

# 設定字體支援中文
import matplotlib.font_manager as fm

# 使用系統字體
font_paths = [
    '/System/Library/Fonts/PingFang.ttc',  # macOS
    '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',  # Linux
]

for path in font_paths:
    try:
        fm.fontManager.addfont(path)
        break
    except:
        pass

plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Arial', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

OUTPUT_DIR = "/Users/lanss/projects/2_Practice/readpaper/the_batch_358/images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================================================
# 圖表 0：AI 供應鏈危機四步演進流
# ============================================================================
def generate_infographic_0():
    """AI 供應鏈危機四步演進流"""
    fig, ax = plt.subplots(figsize=(16, 9), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # 標題
    ax.text(5, 9.3, 'AI 供應鏈危機四步演進流',
            ha='center', va='top', fontsize=28, fontweight='bold')

    # 時間節點數據
    events = [
        {
            'date': '2025/4',
            'name': '限制通知',
            'actors': '美國商務部',
            'global': '舞蹈教室效應',
            'x': 1.5
        },
        {
            'date': '2025/5',
            'name': '隱形降級',
            'actors': 'Anthropic',
            'global': '輿論反彈',
            'x': 3.8
        },
        {
            'date': '2025/6',
            'name': '出口管制',
            'actors': '多國跟進',
            'global': '全球禁用',
            'x': 6.1
        },
        {
            'date': '2025/7',
            'name': '開源投資',
            'actors': '各國反制',
            'global': '供應鏈變革',
            'x': 8.4
        }
    ]

    # 顏色漸層
    colors_gradient = ['#0f172a', '#1e40af', '#f97316', '#ea580c']

    for i, event in enumerate(events):
        x = event['x']

        # 時間節點圓形
        circle = plt.Circle((x, 7), 0.35, color=colors_gradient[i], zorder=10)
        ax.add_patch(circle)
        ax.text(x, 7, str(i), ha='center', va='center',
                fontsize=16, fontweight='bold', color='white', zorder=11)

        # 連接線
        if i < len(events) - 1:
            ax.arrow(x + 0.35, 7, events[i+1]['x'] - x - 0.7, 0,
                    head_width=0.2, head_length=0.15, fc=colors_gradient[i],
                    ec=colors_gradient[i], alpha=0.6, zorder=5)

        # 事件卡片
        # 日期
        ax.text(x, 6.2, event['date'], ha='center', va='top',
                fontsize=13, fontweight='bold')

        # 事件名稱
        ax.text(x, 5.9, event['name'], ha='center', va='top',
                fontsize=12, fontweight='bold', color='#1e40af')

        # 影響方
        ax.text(x, 5.5, f"▸ {event['actors']}", ha='center', va='top',
                fontsize=10, style='italic')

        # 全球反應
        ax.text(x, 5.1, f"◆ {event['global']}", ha='center', va='top',
                fontsize=10, color='#dc2626')

    # 底部統計框
    stat_box = FancyBboxPatch((0.3, 0.3), 9.4, 1.2,
                              boxstyle="round,pad=0.1",
                              edgecolor='#1e40af', facecolor='#eff6ff',
                              linewidth=2, zorder=1)
    ax.add_patch(stat_box)

    ax.text(2.5, 1.2, '開源 AI 投資↑40%', ha='center', va='center',
            fontsize=13, fontweight='bold', color='#1e40af')
    ax.text(5, 1.2, '進口限制↑25%', ha='center', va='center',
            fontsize=13, fontweight='bold', color='#dc2626')
    ax.text(7.5, 1.2, '地緣政治風險↑60%', ha='center', va='center',
            fontsize=13, fontweight='bold', color='#ea580c')

    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/infographic_0_supply_chain_escalation.png",
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 圖表 0 已生成：supply_chain_escalation.png")


# ============================================================================
# 圖表 1：Fable 5 降級風波時間線
# ============================================================================
def generate_infographic_1():
    """Fable 5 降級風波時間線"""
    fig, ax = plt.subplots(figsize=(16, 9), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # 標題
    ax.text(5, 9.5, 'Fable 5 隱形降級風波時間線',
            ha='center', va='top', fontsize=28, fontweight='bold')
    ax.text(5, 9, '從廠商控制到市場衝擊的 4 週演進',
            ha='center', va='top', fontsize=14, style='italic', color='#666')

    # 中心垂直時間線
    ax.plot([5, 5], [1, 8], 'k-', linewidth=3, zorder=1)

    # 5 個事件節點
    events = [
        {
            'week': 'T0',
            'date': '4月15日',
            'event': '發布新版限制',
            'detail': '精英市場限制',
            'severity': '#fcd34d',
            'y': 7.5,
            'side': 'left'
        },
        {
            'week': 'T+1w',
            'date': '4月22日',
            'event': '隱形降級發現',
            'detail': '功能暗中削弱',
            'severity': '#f97316',
            'y': 6,
            'side': 'right'
        },
        {
            'week': 'T+2w',
            'date': '4月29日',
            'event': '輿論反彈',
            'detail': '用戶激烈抗議',
            'severity': '#dc2626',
            'y': 4.5,
            'side': 'left'
        },
        {
            'week': 'T+3w',
            'date': '5月6日',
            'event': '出口管制擴展',
            'detail': '多國聯動限制',
            'severity': '#b91c1c',
            'y': 3,
            'side': 'right'
        },
        {
            'week': 'T+4w',
            'date': '5月13日',
            'event': '全球禁用',
            'detail': '多國停用 Fable',
            'severity': '#7f1d1d',
            'y': 1.5,
            'side': 'left'
        }
    ]

    for event in events:
        x = 3 if event['side'] == 'left' else 7
        y = event['y']

        # 連接線
        ax.plot([5, x], [y, y], 'k-', linewidth=1, alpha=0.3, zorder=1)

        # 事件圓點
        circle = plt.Circle((5, y), 0.25, color=event['severity'],
                           edgecolor='black', linewidth=2, zorder=10)
        ax.add_patch(circle)

        # 事件卡片背景
        card_width = 1.5
        card_height = 0.8
        card_x = x - card_width/2 if event['side'] == 'left' else x - card_width/2

        card = FancyBboxPatch((card_x, y - card_height/2), card_width, card_height,
                             boxstyle="round,pad=0.05",
                             edgecolor=event['severity'], facecolor='white',
                             linewidth=2, zorder=5)
        ax.add_patch(card)

        # 卡片文字
        ax.text(x, y + 0.3, event['week'], ha='center', va='center',
               fontsize=11, fontweight='bold', color='#1e40af')
        ax.text(x, y, event['date'], ha='center', va='center',
               fontsize=9, color='#666')
        ax.text(x, y - 0.35, event['event'], ha='center', va='center',
               fontsize=10, fontweight='bold', color=event['severity'])

    # 圖示說明
    icons_y = 0.3
    ax.text(1, icons_y, '🔒 限制', fontsize=11, ha='left', va='center')
    ax.text(3, icons_y, '⚠️ 風險', fontsize=11, ha='left', va='center')
    ax.text(5, icons_y, '🌍 全球', fontsize=11, ha='left', va='center')
    ax.text(7, icons_y, '📊 數據', fontsize=11, ha='left', va='center')

    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/infographic_1_fable_timeline.png",
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 圖表 1 已生成：fable_timeline.png")


# ============================================================================
# 圖表 2：評測基準演進對比
# ============================================================================
def generate_infographic_2():
    """評測基準演進對比（SWE-bench → DeepSWE/ProgramBench/ITBench-AA）"""
    fig, ax = plt.subplots(figsize=(16, 9), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # 標題
    ax.text(5, 9.5, '評測基準演進：從編碼到系統思維',
            ha='center', va='top', fontsize=28, fontweight='bold')

    # 基準對比
    benchmarks = [
        {
            'name': 'SWE-bench',
            'type': '代碼修復',
            'difficulty': '★★',
            'size': '100 行代碼',
            'performance': '90%',
            'model': '各類模型',
            'x': 1.5,
            'color': '#d1d5db'
        },
        {
            'name': 'DeepSWE',
            'type': '特徵實作',
            'difficulty': '★★★★',
            'size': '550 行代碼',
            'performance': '70%',
            'model': 'GPT-5.5',
            'x': 4,
            'color': '#3b82f6'
        },
        {
            'name': 'ProgramBench',
            'type': '程序合成',
            'difficulty': '★★★★★',
            'size': '真實可執行',
            'performance': '3%',
            'model': 'Claude Opus 4.7',
            'x': 6.5,
            'color': '#f97316'
        },
        {
            'name': 'ITBench-AA',
            'type': '根因診斷',
            'difficulty': '★★★★★',
            'size': '現代基礎設施',
            'performance': '46.7%',
            'model': 'Claude Opus 4.7',
            'x': 9,
            'color': '#ea580c'
        }
    ]

    for benchmark in benchmarks:
        x = benchmark['x']

        # 基準卡片背景
        card = FancyBboxPatch((x - 0.9, 2), 1.8, 6.2,
                             boxstyle="round,pad=0.1",
                             edgecolor=benchmark['color'],
                             facecolor='white',
                             linewidth=3, zorder=5)
        ax.add_patch(card)

        # 標題
        ax.text(x, 7.9, benchmark['name'], ha='center', va='center',
               fontsize=13, fontweight='bold', color=benchmark['color'])

        # 類別
        ax.text(x, 7.4, benchmark['type'], ha='center', va='center',
               fontsize=11, color='#333', style='italic')

        # 難度
        ax.text(x, 6.8, f"難度: {benchmark['difficulty']}",
               ha='center', va='center', fontsize=10, color='#666')

        # 規模
        ax.text(x, 6.3, benchmark['size'], ha='center', va='center',
               fontsize=10, color='#666')

        # 性能
        perf_color = '#dc2626' if float(benchmark['performance'].rstrip('%')) < 50 else '#10b981'
        ax.text(x, 5.6, f"性能: {benchmark['performance']}",
               ha='center', va='center', fontsize=11, fontweight='bold',
               color=perf_color)

        # 模型
        ax.text(x, 5.0, f"最優: {benchmark['model']}",
               ha='center', va='center', fontsize=10, color='#666')

        # 分隔線
        if x < 9:
            ax.plot([x + 0.9, x + 0.9], [2.2, 7.8], 'k--', alpha=0.2, linewidth=1)

    # 中心箭頭和洞察
    ax.annotate('', xy=(5, 1.5), xytext=(2, 1.5),
                arrowprops=dict(arrowstyle='->', lw=3, color='#1e40af'))
    ax.text(3.5, 1.2, '能力邊界演進', ha='center', va='top',
           fontsize=12, fontweight='bold', color='#1e40af')
    ax.text(3.5, 0.8, '從代碼編輯 → 系統診斷', ha='center', va='top',
           fontsize=11, color='#666', style='italic')

    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/infographic_2_benchmark_evolution.png",
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 圖表 2 已生成：benchmark_evolution.png")


# ============================================================================
# 圖表 3：Nemotron 3 Ultra 架構圖
# ============================================================================
def generate_infographic_3():
    """Nemotron 3 Ultra 架構圖"""
    fig, ax = plt.subplots(figsize=(16, 9), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # 標題
    ax.text(5, 9.5, 'Nemotron 3 Ultra：混合架構突破',
            ha='center', va='top', fontsize=28, fontweight='bold')

    # 頂部規格
    specs_box = FancyBboxPatch((0.5, 8.5), 9, 0.8,
                              boxstyle="round,pad=0.05",
                              edgecolor='#1e40af', facecolor='#eff6ff',
                              linewidth=2)
    ax.add_patch(specs_box)

    ax.text(1.5, 8.9, '550B 參數', ha='center', va='center',
           fontsize=11, fontweight='bold', color='#1e40af')
    ax.text(3.2, 8.9, '55B active/token', ha='center', va='center',
           fontsize=11, fontweight='bold', color='#1e40af')
    ax.text(5, 8.9, '183 tokens/sec', ha='center', va='center',
           fontsize=11, fontweight='bold', color='#1e40af')
    ax.text(7, 8.9, '1M 上下文', ha='center', va='center',
           fontsize=11, fontweight='bold', color='#1e40af')

    # 中心架構層疊
    layers_y = 7.5
    layer_configs = [
        {'name': 'Mamba', 'color': '#3b82f6', 'benefit': '📉 低內存', 'y': layers_y},
        {'name': 'Self-Attn', 'color': '#10b981', 'benefit': '🎯 高精度召回', 'y': layers_y - 0.9},
        {'name': 'LatentMoE', 'color': '#f97316', 'benefit': '⚡ 路由到 10 專家', 'y': layers_y - 1.8},
    ]

    for i, layer in enumerate(layer_configs):
        box = FancyBboxPatch((2, layer['y'] - 0.3), 6, 0.6,
                            boxstyle="round,pad=0.05",
                            edgecolor=layer['color'], facecolor='white',
                            linewidth=2)
        ax.add_patch(box)

        ax.text(3.5, layer['y'], f"[{layer['name']}]", ha='center', va='center',
               fontsize=12, fontweight='bold', color=layer['color'])
        ax.text(7, layer['y'], layer['benefit'], ha='left', va='center',
               fontsize=11, color='#666')

        if i < len(layer_configs) - 1:
            ax.annotate('', xy=(5, layer['y'] - 0.35), xytext=(5, layer['y'] - 0.35 - 0.25),
                       arrowprops=dict(arrowstyle='->', lw=2, color='#666'))

    # 訓練管道
    train_y = 3.8
    ax.text(5, train_y, '訓練管道（4 階段）', ha='center', va='center',
           fontsize=13, fontweight='bold', color='#1e40af')

    train_steps = [
        {'step': '1️⃣ 預訓練', 'desc': '20T tokens', 'x': 1.8},
        {'step': '2️⃣ SFT+RL', 'desc': '6 個領域', 'x': 4},
        {'step': '3️⃣ 多師蒸餾', 'desc': '10+ 域專家', 'x': 6.2},
        {'step': '4️⃣ 評估', 'desc': '47.7% NVFP4', 'x': 8.4},
    ]

    for step in train_steps:
        box = FancyBboxPatch((step['x'] - 0.7, train_y - 1.5), 1.4, 1,
                            boxstyle="round,pad=0.05",
                            edgecolor='#f97316', facecolor='#fff7ed',
                            linewidth=2)
        ax.add_patch(box)

        ax.text(step['x'], train_y - 0.8, step['step'], ha='center', va='center',
               fontsize=10, fontweight='bold', color='#ea580c')
        ax.text(step['x'], train_y - 1.2, step['desc'], ha='center', va='center',
               fontsize=9, color='#666')

        if step['x'] < 8:
            ax.annotate('', xy=(step['x'] + 0.75, train_y - 1),
                       xytext=(step['x'] + 0.7, train_y - 1),
                       arrowprops=dict(arrowstyle='->', lw=2, color='#666'))

    # 性能對比
    perf_y = 0.8
    ax.text(2.5, perf_y, 'NVFP4: 47.7%', ha='center', va='center',
           fontsize=11, fontweight='bold', color='#1e40af')
    ax.text(5, perf_y, '完整精度: 48.2%', ha='center', va='center',
           fontsize=11, fontweight='bold', color='#10b981')
    ax.text(7.5, perf_y, '+21~44% vs 美國開源', ha='center', va='center',
           fontsize=11, fontweight='bold', color='#ea580c')

    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/infographic_3_nemotron_architecture.png",
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 圖表 3 已生成：nemotron_architecture.png")


# ============================================================================
# 圖表 4：地緣政治供應鏈脆弱性演進
# ============================================================================
def generate_infographic_4():
    """地緣政治供應鏈脆弱性演進"""
    fig, ax = plt.subplots(figsize=(16, 9), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # 標題
    ax.text(5, 9.5, '地緣政治供應鏈脆弱性演進',
            ha='center', va='top', fontsize=28, fontweight='bold')
    ax.text(5, 9, '一旦存取被威脅，國家大幅投資替代方案',
            ha='center', va='top', fontsize=13, style='italic', color='#666')

    # 三個歷史階段
    stages = [
        {
            'name': '半導體供應鏈',
            'period': '2018-2022',
            'trigger': '美國限制中國晶片',
            'response': '中國投資↑300%',
            'x': 1.8,
            'color': '#3b82f6'
        },
        {
            'name': '稀土礦物',
            'period': '2010-2020',
            'trigger': '中國限制日本稀土',
            'response': '多元化應對',
            'x': 5,
            'color': '#f97316'
        },
        {
            'name': 'AI 模型',
            'period': '2025 現在',
            'trigger': '美國管制 Fable/Mythos',
            'response': '全球投資開源',
            'x': 8.2,
            'color': '#ea580c'
        }
    ]

    for stage in stages:
        # 階段卡片
        card = FancyBboxPatch((stage['x'] - 1.2, 3), 2.4, 5,
                             boxstyle="round,pad=0.1",
                             edgecolor=stage['color'],
                             facecolor='white',
                             linewidth=3)
        ax.add_patch(card)

        # 階段名稱
        ax.text(stage['x'], 7.7, stage['name'], ha='center', va='center',
               fontsize=13, fontweight='bold', color=stage['color'])

        # 時期
        ax.text(stage['x'], 7.2, stage['period'], ha='center', va='center',
               fontsize=10, color='#666', style='italic')

        # 分隔線
        ax.plot([stage['x'] - 1, stage['x'] + 1], [6.9, 6.9],
               color=stage['color'], linewidth=1, alpha=0.5)

        # 觸發因素
        ax.text(stage['x'], 6.4, '觸發因素', ha='center', va='center',
               fontsize=10, fontweight='bold', color='#666')
        ax.text(stage['x'], 5.9, stage['trigger'], ha='center', va='center',
               fontsize=9, color='#dc2626', style='italic', wrap=True)

        # 分隔線
        ax.plot([stage['x'] - 1, stage['x'] + 1], [5.5, 5.5],
               color=stage['color'], linewidth=1, alpha=0.5)

        # 國家反應
        ax.text(stage['x'], 5, '國家反應', ha='center', va='center',
               fontsize=10, fontweight='bold', color='#666')
        ax.text(stage['x'], 4.4, stage['response'], ha='center', va='center',
               fontsize=9, fontweight='bold', color='#10b981')

        # 連接箭頭
        if stage['x'] < 8:
            ax.annotate('', xy=(stage['x'] + 1.3, 5.5),
                       xytext=(stage['x'] + 1.2, 5.5),
                       arrowprops=dict(arrowstyle='->', lw=2, color='#666'))

    # 底部洞察框
    insight_box = FancyBboxPatch((0.3, 0.2), 9.4, 2.2,
                                boxstyle="round,pad=0.1",
                                edgecolor='#1e40af', facecolor='#eff6ff',
                                linewidth=2)
    ax.add_patch(insight_box)

    ax.text(5, 2, '📌 核心洞察', ha='center', va='center',
           fontsize=12, fontweight='bold', color='#1e40af')
    ax.text(5, 1.5, '一旦存取被威脅，國家大幅投資替代方案', ha='center', va='center',
           fontsize=11, color='#333')

    ax.text(2.2, 0.8, '🚫 禁用效應', ha='center', va='center',
           fontsize=10, color='#dc2626', fontweight='bold')
    ax.text(5, 0.8, '💰 投資激增', ha='center', va='center',
           fontsize=10, color='#10b981', fontweight='bold')
    ax.text(7.8, 0.8, '🏭 基礎設施競賽', ha='center', va='center',
           fontsize=10, color='#ea580c', fontweight='bold')

    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/infographic_4_geopolitical_supply_chain.png",
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ 圖表 4 已生成：geopolitical_supply_chain.png")


# ============================================================================
# 圖表 5：POPE 訓練流程圖（4 階段）
# ============================================================================
def generate_infographic_5():
    """POPE 訓練流程圖（4 階段）"""
    fig, ax = plt.subplots(figsize=(16, 9), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # 標題
    ax.text(5, 9.5, 'POPE：從難題到解法的漸進學習',
            ha='center', va='top', fontsize=28, fontweight='bold')

    # 4 個訓練階段
    stages = [
        {
            'num': '1️⃣',
            'title': '問題篩選',
            'detail': ['難題篩選', '(AIME/HMMT)', '模型失敗', '128+ 次'],
            'x': 1.8,
            'color': '#3b82f6'
        },
        {
            'num': '2️⃣',
            'title': '前綴提取',
            'detail': ['逐步增長', '前綴長度', '1/4 → 1/2', '→ 3/4 → 全'],
            'x': 4,
            'color': '#10b981'
        },
        {
            'num': '3️⃣',
            'title': 'GRPO 訓練',
            'detail': ['雙版本', '50% 帶 hint', '50% 無 hint', '並行訓練'],
            'x': 6.2,
            'color': '#f97316'
        },
        {
            'num': '4️⃣',
            'title': '漸進移除',
            'detail': ['迭代去除', '提示詞', '從中點 → 起點', '逐步獨立'],
            'x': 8.4,
            'color': '#ea580c'
        }
    ]

    for i, stage in enumerate(stages):
        # 階段卡片
        card = FancyBboxPatch((stage['x'] - 0.9, 5.5), 1.8, 2.8,
                             boxstyle="round,pad=0.1",
                             edgecolor=stage['color'],
                             facecolor='white',
                             linewidth=2)
        ax.add_patch(card)

        # 編號
        ax.text(stage['x'], 8.1, stage['num'], ha='center', va='center',
               fontsize=14, fontweight='bold')

        # 標題
        ax.text(stage['x'], 7.7, stage['title'], ha='center', va='center',
               fontsize=11, fontweight='bold', color=stage['color'])

        # 詳情
        y_offset = 7.2
        for detail_line in stage['detail']:
            ax.text(stage['x'], y_offset, detail_line, ha='center', va='center',
                   fontsize=9, color='#666')
            y_offset -= 0.45

        # 連接箭頭
        if i < len(stages) - 1:
            ax.annotate('', xy=(stages[i+1]['x'] - 0.95, 6.9),
                       xytext=(stage['x'] + 0.9, 6.9),
                       arrowprops=dict(arrowstyle='->', lw=2.5, color='#666'))

    # 結果對比條形圖
    results_y_base = 4.5

    ax.text(5, results_y_base + 0.5, '📊 性能結果對比', ha='center', va='top',
           fontsize=13, fontweight='bold', color='#1e40af')

    # AIME 2025 結果
    aime_y = results_y_base - 0.8
    ax.text(0.8, aime_y + 0.3, 'AIME 2025', ha='center', va='center',
           fontsize=11, fontweight='bold')

    # pass@1
    ax.text(0.8, aime_y - 0.2, 'pass@1', ha='center', va='center',
           fontsize=9, color='#666')

    # 正規化條形圖（0-10 範圍）
    # SFT ~30%
    bar_width = 0.2
    bar1_width = 3.0  # 30% of 10
    ax.barh(aime_y - 0.6, bar1_width, height=bar_width, left=1.5, color='#d1d5db')
    ax.text(1.5 + bar1_width + 0.2, aime_y - 0.6, '~30%', ha='left', va='center', fontsize=9)

    # GRPO 49.6%
    bar2_width = 4.96  # 49.6% of 10
    ax.barh(aime_y - 0.85, bar2_width, height=bar_width, left=1.5, color='#3b82f6')
    ax.text(1.5 + bar2_width + 0.2, aime_y - 0.85, '49.6%', ha='left', va='center', fontsize=9)

    # POPE 53.1%
    bar3_width = 5.31  # 53.1% of 10
    ax.barh(aime_y - 1.1, bar3_width, height=bar_width, left=1.5, color='#10b981')
    ax.text(1.5 + bar3_width + 0.2, aime_y - 1.1, '53.1% ⬆️', ha='left', va='center',
           fontsize=9, color='#10b981', fontweight='bold')

    # HMMT 2025 結果
    hmmt_y = aime_y - 2
    ax.text(0.8, hmmt_y + 0.3, 'HMMT 2025', ha='center', va='center',
           fontsize=11, fontweight='bold')

    ax.text(0.8, hmmt_y - 0.2, 'pass@1', ha='center', va='center',
           fontsize=9, color='#666')

    # GRPO 31.0%
    bar4_width = 3.1
    ax.barh(hmmt_y - 0.6, bar4_width, height=bar_width, left=1.5, color='#3b82f6')
    ax.text(1.5 + bar4_width + 0.2, hmmt_y - 0.6, '31.0%', ha='left', va='center', fontsize=9)

    # POPE 37.8%
    bar5_width = 3.78
    ax.barh(hmmt_y - 0.85, bar5_width, height=bar_width, left=1.5, color='#10b981')
    ax.text(1.5 + bar5_width + 0.2, hmmt_y - 0.85, '37.8% ⬆️ (+22%)', ha='left', va='center',
           fontsize=9, color='#10b981', fontweight='bold')

    # 教育洞察框
    insight_box = FancyBboxPatch((0.2, 0.1), 9.6, 0.9,
                                boxstyle="round,pad=0.05",
                                edgecolor='#f97316', facecolor='#fff7ed',
                                linewidth=2)
    ax.add_patch(insight_box)

    ax.text(5, 0.8, '💡 POPE 核心優勢', ha='center', va='center',
           fontsize=11, fontweight='bold', color='#ea580c')
    ax.text(5, 0.4, '將難題學習分 2 階段：先有提示學習機制，再逐步去除依賴，提升單次通過率 22%',
           ha='center', va='center', fontsize=10, color='#333')

    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/infographic_5_pope_training_flow.png",
                dpi=300, bbox_inches='tight', facecolor='white', pad_inches=0.3)
    plt.close()
    print("✓ 圖表 5 已生成：pope_training_flow.png")


# ============================================================================
# 圖表 6：POPE vs GRPO 性能對比（2 數據集）
# ============================================================================
def generate_infographic_6():
    """POPE vs GRPO 性能對比（2 數據集）"""
    fig, ax = plt.subplots(figsize=(16, 9), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # 標題
    ax.text(5, 9.5, 'POPE vs GRPO：性能對比分析',
            ha='center', va='top', fontsize=28, fontweight='bold')
    ax.text(5, 9, '🎯 實時資安事件回應的單次通過率優化',
            ha='center', va='top', fontsize=13, style='italic', color='#666')

    # AIME 2025 結果（左側）
    aime_x = 2.5
    ax.text(aime_x, 8.5, 'AIME 2025', ha='center', va='center',
           fontsize=14, fontweight='bold', color='#1e40af')

    # pass@1 結果
    ax.text(aime_x, 8, 'pass@1', ha='center', va='center',
           fontsize=11, fontweight='bold', color='#333')

    results_aime = [
        {'name': 'SFT', 'value': 30, 'color': '#d1d5db', 'y': 7.4},
        {'name': 'GRPO', 'value': 49.6, 'color': '#3b82f6', 'y': 6.9},
        {'name': 'POPE', 'value': 53.1, 'color': '#10b981', 'y': 6.4, 'note': '⬆️ +3.5pp'}
    ]

    for res in results_aime:
        # 條形圖（正規化到 0-2 範圍）
        bar_width = res['value'] / 100 * 2
        rect = mpatches.Rectangle((aime_x - 1, res['y'] - 0.15), bar_width, 0.3,
                                   facecolor=res['color'], edgecolor='black', linewidth=1)
        ax.add_patch(rect)
        ax.text(aime_x - 1.15, res['y'], res['name'], ha='right', va='center',
               fontsize=10, fontweight='bold')
        ax.text(aime_x - 1 + bar_width + 0.1, res['y'], f"{res['value']:.1f}%", ha='left', va='center',
               fontsize=10, fontweight='bold', color=res['color'] if res['color'] != '#d1d5db' else '#666')
        if 'note' in res:
            ax.text(aime_x - 1 + bar_width + 0.8, res['y'], res['note'], ha='left', va='center',
                   fontsize=9, color='#10b981', fontweight='bold')

    # HMMT 2025 結果（右側）
    hmmt_x = 7.5
    ax.text(hmmt_x, 8.5, 'HMMT 2025', ha='center', va='center',
           fontsize=14, fontweight='bold', color='#f97316')

    # pass@1 結果
    ax.text(hmmt_x, 8, 'pass@1', ha='center', va='center',
           fontsize=11, fontweight='bold', color='#333')

    results_hmmt = [
        {'name': 'GRPO', 'value': 31.0, 'color': '#3b82f6', 'y': 7.4},
        {'name': 'POPE', 'value': 37.8, 'color': '#10b981', 'y': 6.9, 'note': '⬆️ +22%'}
    ]

    for res in results_hmmt:
        # 條形圖（正規化到 0-2 範圍）
        bar_width = res['value'] / 100 * 2
        rect = mpatches.Rectangle((hmmt_x - 1, res['y'] - 0.15), bar_width, 0.3,
                                   facecolor=res['color'], edgecolor='black', linewidth=1)
        ax.add_patch(rect)
        ax.text(hmmt_x - 1.15, res['y'], res['name'], ha='right', va='center',
               fontsize=10, fontweight='bold')
        ax.text(hmmt_x - 1 + bar_width + 0.1, res['y'], f"{res['value']:.1f}%", ha='left', va='center',
               fontsize=10, fontweight='bold', color=res['color'])
        if 'note' in res:
            ax.text(hmmt_x - 1 + bar_width + 0.8, res['y'], res['note'], ha='left', va='center',
                   fontsize=9, color='#10b981', fontweight='bold')

    # 圖例
    legend_y = 5.5
    ax.text(1.5, legend_y, '■ SFT', fontsize=10, color='#666')
    ax.text(2.8, legend_y, '■ GRPO', fontsize=10, color='#3b82f6', fontweight='bold')
    ax.text(4.2, legend_y, '■ POPE', fontsize=10, color='#10b981', fontweight='bold')

    # pass@16 提示
    ax.text(5, 4.8, 'pass@16 邊際提升（改進有限）', ha='center', va='center',
           fontsize=10, color='#999', style='italic')

    # 核心洞察
    insight_box = FancyBboxPatch((0.3, 0.1), 9.4, 3.5,
                                boxstyle="round,pad=0.1",
                                edgecolor='#1e40af', facecolor='#eff6ff',
                                linewidth=2)
    ax.add_patch(insight_box)

    ax.text(5, 3.4, '🔍 關鍵發現', ha='center', va='center',
           fontsize=13, fontweight='bold', color='#1e40af')

    insights = [
        '✓ POPE 在 pass@1（單次通過）優勢最強：AIME +3.5pp，HMMT +22% 相對',
        '✓ 核心優勢：難題學習分 2 階段 - 先有 hint 學習，再逐步去除',
        '✓ 應用場景：實時資安事件回應需要單次通過率（無重試機會）'
    ]

    y_pos = 2.9
    for insight in insights:
        ax.text(5, y_pos, insight, ha='center', va='center',
               fontsize=9, color='#333')
        y_pos -= 0.6

    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/infographic_6_pope_performance_comparison.png",
                dpi=300, bbox_inches='tight', facecolor='white', pad_inches=0.2)
    plt.close()
    print("✓ 圖表 6 已生成：pope_performance_comparison.png")


# ============================================================================
# 執行所有生成
# ============================================================================
def main():
    print("\n🚀 開始生成 7 個信息圖表...\n")

    try:
        generate_infographic_0()
        generate_infographic_1()
        generate_infographic_2()
        generate_infographic_3()
        generate_infographic_4()
        generate_infographic_5()
        generate_infographic_6()

        print("\n✅ 所有圖表已成功生成！")
        print(f"📁 輸出目錄：{OUTPUT_DIR}\n")

        # 列出所有生成的文件
        import glob
        files = sorted(glob.glob(f"{OUTPUT_DIR}/infographic_*.png"))
        print("📋 已生成的文件清單：")
        for f in files:
            file_size = os.path.getsize(f) / 1024 / 1024
            print(f"   • {os.path.basename(f)} ({file_size:.1f} MB)")

    except Exception as e:
        print(f"❌ 錯誤：{e}")
        raise

if __name__ == "__main__":
    main()
