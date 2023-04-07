import requests
from bs4 import BeautifulSoup

url = 'https://tunebat.com/Analyzer'

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': 'ARRAffinity=7566f613b0c7a36333f4bcbc6204793ede6da2b122bb0a7442bef2e3c1d11190; ARRAffinitySameSite=7566f613b0c7a36333f4bcbc6204793ede6da2b122bb0a7442bef2e3c1d11190; ai_user=hV65Cp1Usd3sSj6RIArtTm|2023-04-05T18:35:36.233Z; __cf_bm=ZJq6LAhrGOHkghV5Z3ibXny8vivUMSdr5UEz1mdl9nw-1680719760-0-AVf1uLruSSu8rem+ihQo0UpUAlmVjNjKZooAjCSwQu4n+NlSxC58Ach5KfjFBOQskmtZXDyCCa5pEa7o/JT7xg0wSENPPRy7xVA2AuCi4KvKfJZwRyN11m1aTK7zvpuHRw==; ai_session=/WnQfLQ48IBEJpgY/VPia/|1680719736448|1680720475933',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}
req = requests.get(url, headers=headers)
print(req.status_code)
# src = req.text

# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(src)

