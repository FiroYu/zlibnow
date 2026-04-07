"""
IndexNow - Submit URLs to Bing and other search engines for instant indexing.
Run after deploying changes: py indexnow.py
"""
import json
import urllib.request

API_KEY = "60a2cf10501541765be9c51c879bebd4"
HOST = "zlibnow.com"

URLS = [
    "https://zlibnow.com/",
    "https://zlibnow.com/zh/",
    "https://zlibnow.com/es/",
    "https://zlibnow.com/fr/",
    "https://zlibnow.com/de/",
    "https://zlibnow.com/it/",
    "https://zlibnow.com/ja/",
    "https://zlibnow.com/ko/",
    "https://zlibnow.com/ru/",
    "https://zlibnow.com/ar/",
]

payload = {
    "host": HOST,
    "key": API_KEY,
    "urlList": URLS,
}

endpoints = [
    f"https://api.indexnow.org/indexnow?key={API_KEY}",
    f"https://www.bing.com/indexnow?url=https://zlibnow.com/&key={API_KEY}",
]

for endpoint in endpoints:
    try:
        req = urllib.request.Request(
            endpoint,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        resp = urllib.request.urlopen(req, timeout=30)
        print(f"[OK] {endpoint.split('?')[0]} -> {resp.status}")
    except Exception as e:
        print(f"[ERR] {endpoint.split('?')[0]} -> {e}")

print("Done.")
