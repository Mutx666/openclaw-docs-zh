import os
import requests
import xml.etree.ElementTree as ET
import subprocess
import time

SITEMAP_URL = "https://docs.openclaw.ai/sitemap.xml"
OPENCODE_PATH = "/home/mutx163/.opencode/bin/opencode"
TARGET_DIR = "/home/mutx163/openclaw-docs-zh"

def get_urls():
    r = requests.get(SITEMAP_URL)
    root = ET.fromstring(r.text)
    urls = []
    for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
        loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
        urls.append(loc)
    return urls

def translate_and_save(url):
    relative_path = url.replace("https://docs.openclaw.ai/", "")
    if not relative_path or relative_path == "":
        relative_path = "index"
    
    file_path = os.path.join(TARGET_DIR, f"{relative_path}.md")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    print(f"Processing: {url} -> {file_path}")
    
    # Use OpenCode to fetch, translate and save
    prompt = f"Fetch the content of {url}, translate it into professional Chinese, keeping the Markdown format and structure exactly same. Save the translated content to {file_path}."
    cmd = [OPENCODE_PATH, "run", "--model", "opencode/kimi-k2.5-free", prompt]
    
    try:
        subprocess.run(cmd, check=True)
        # Commit and push after each file
        subprocess.run(["git", "add", file_path], cwd=TARGET_DIR)
        subprocess.run(["git", "commit", "-m", f"Translated: {relative_path}"], cwd=TARGET_DIR)
        subprocess.run(["git", "push", "origin", "main"], cwd=TARGET_DIR)
        return True
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return False

def main():
    urls = get_urls()
    print(f"Found {len(urls)} pages.")
    for url in urls[:5]: # Start with first 5 for testing/initial batch
        translate_and_save(url)
        time.sleep(2)

if __name__ == "__main__":
    main()
