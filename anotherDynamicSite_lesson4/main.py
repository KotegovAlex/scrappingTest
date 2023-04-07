import requests
import json
import lxml
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

fests_urls_list = []

# for i in range(0, 264, 24):
for i in range(0, 24, 24):

    url = f'https://www.skiddle.com/festivals/search/?ajaxing=1&sort=2&fest_name=&from_date=6%20Apr%202023&to_date=&maxprice=500&o={i}&bannertitle='

    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    html_response = json_data["html"]

    with open(f"data/index_{i}.html", "w") as file:
        file.write(html_response)

    with open(f"data/index_{i}.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    cards = soup.find_all("a", class_="card-details-link")
    for item in cards:
        fest_url = 'https://www.skiddle.com' + item.get("href")
        fests_urls_list.append(fest_url)

for url in fests_urls_list:
    req = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(req.text, "lxml")
    fest_info_block = soup.find("div", class_="top-info-cont")
