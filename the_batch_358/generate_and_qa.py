import subprocess
import json
import time

commands = [
    [
        "python3", "/Users/lanss/.gemini/skills/md_to_html/scripts/codex_imagegen.py",
        "--prompt", "手寫筆記風格（sketchnote、hand-drawn doodle style）。生成資訊圖表總結四大重點，標題與標籤一律用手寫字體，米白筆記紙背景。使用台灣 IT／AI 繁體中文，粉圓體，16:9。重點：1. 數位水電中斷（供應鏈風險）、2. 黑盒防禦死局（稽核盲區）、3. 新評測指標（ITBench）、4. 地緣政治與AI主權。結構：手繪區塊組合。",
        "--image", "images/summary.png",
        "--aspect", "16:9"
    ],
    [
        "python3", "/Users/lanss/.gemini/skills/md_to_html/scripts/codex_imagegen.py",
        "--prompt", "依據原始 16:9 資訊圖內容，重新繪製成 9:16 直式版本，手寫筆記風格（sketchnote、hand-drawn doodle style），米白筆記紙背景。務必保留並重現視覺元素：四大重點區塊「數位水電中斷」、「黑盒防禦死局」、「新評測指標」、「地緣政治與AI主權」，請垂直排列。",
        "--image", "images/summary-mobile.png",
        "--aspect", "9:16"
    ],
    [
        "python3", "/Users/lanss/.gemini/skills/md_to_html/scripts/codex_imagegen.py",
        "--prompt", "生成資訊圖表，表達白話易懂，使用台灣 IT／資安／AI 專業用語繁體中文，粉圓體，科技感扁平風格，16:9。段落主題：Claude Fable 5 雙層過濾與隱形降級機制。重點：API直接拒絕(紅色阻擋) vs 工具模式悄悄路由到較弱的 Opus 4.8(藍色虛線)。結構：流程對照圖。",
        "--image", "images/fable_mechanism.png",
        "--aspect", "16:9"
    ],
    [
        "python3", "/Users/lanss/.gemini/skills/md_to_html/scripts/codex_imagegen.py",
        "--prompt", "依據原始 16:9 資訊圖內容，重新繪製成 9:16 直式版本，科技感扁平風格。務必保留並重現視覺元素：Claude Fable 5 雙層過濾流程，上層是 API 直接拒絕(紅色阻擋)，下層是路由到 Opus 4.8(藍色虛線)，請垂直排列。",
        "--image", "images/fable_mechanism-mobile.png",
        "--aspect", "9:16"
    ]
]

generated_count = 0
failed_count = 0

for cmd in commands:
    print(f"Generating image: {cmd[4]}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    try:
        out_json = json.loads(result.stdout.strip())
        if out_json.get("status") == "ok":
            generated_count += 1
            print(f"Success: {out_json['path']}")
        else:
            failed_count += 1
            print(f"Failed: {out_json.get('error')}")
    except Exception as e:
        failed_count += 1
        print(f"Error parsing output: {e}, Raw: {result.stdout}")

print(f"Images generation complete. Success: {generated_count}, Failed: {failed_count}")

# Playwright QA
print("Running Playwright QA...")
qa_script = """
from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width':1280,'height':800})
    file_url = f"file://{os.path.abspath('index.html')}"
    pg.goto(file_url)
    pg.screenshot(path='qa_desktop.png', full_page=True)
    pg.set_viewport_size({'width':390,'height':844})
    pg.screenshot(path='qa_mobile.png', full_page=True)
    b.close()
"""
with open("qa.py", "w") as f:
    f.write(qa_script)

subprocess.run(["python3", "qa.py"])
print("Playwright QA complete. Screenshots saved.")
