import urllib.request
import json
import os
import re

SALON_ID = '65a0a5f8fd89780001162cb6'
BASE_URL = 'https://api.vocus.cc/api/articles'

def fetch_all_articles():
    page = 1
    size = 100
    all_articles = []
    
    while True:
        url = f"{BASE_URL}?salonId={SALON_ID}&page={page}&size={size}"
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')
        
        try:
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode('utf-8'))
                articles = data.get('articles', [])
                if not articles:
                    break
                all_articles.extend(articles)
                
                # 如果回傳的文章數量小於 size，代表已經是最後一頁
                if len(articles) < size:
                    break
                page += 1
        except Exception as e:
            print(f"Error fetching page {page}: {e}")
            break
            
    return all_articles

def filter_ai_900_articles(articles):
    filtered = []
    for article in articles:
        title = article.get('title', '')
        if 'AI-900' in title or '900' in title:
            filtered.append(article)
    return filtered

def fetch_article_content(article_id):
    url = f"https://api.vocus.cc/api/article/{article_id}"
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data.get('article', {}).get('content', '')
    except Exception as e:
        print(f"Error fetching content for {article_id}: {e}")
        return ""

def generate_html_content(title, url, content):
    html = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <style>
        body {{ font-family: 'Inter', sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; line-height: 1.6; color: #333; }}
        img {{ max-width: 100%; height: auto; }}
        a {{ color: #0078D4; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <p><a href="{url}" target="_blank">原文連結</a></p>
    <hr>
    {content}
</body>
</html>"""
    return html

def sanitize_filename(title):
    # 移除不能作為檔名的字元
    title = re.sub(r'[\\/*?:"<>|]', "", title)
    title = title.replace(' ', '_')
    return title

if __name__ == '__main__':
    articles = fetch_all_articles()
    ai_900_articles = filter_ai_900_articles(articles)
    print(f"Fetching full content for {len(ai_900_articles)} articles...")
    
    # 建立 articles 資料夾
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    articles_dir = os.path.join(project_root, 'articles')
    os.makedirs(articles_dir, exist_ok=True)
    
    for a in ai_900_articles:
        content = fetch_article_content(a['_id'])
        url = f"https://vocus.cc/article/{a['_id']}"
        html_str = generate_html_content(a['title'], url, content)
        
        filename = sanitize_filename(a['title']) + '.html'
        filepath = os.path.join(articles_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_str)
            
        print(f"- Saved: {filename}")
