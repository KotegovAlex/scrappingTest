
from bs4 import BeautifulSoup

with open('index.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

# title = soup.title
# print(title.string)
# page_all_h1 = soup.findAll("h1")
# print(page_all_h1)

# for item in page_all_h1:
#     print(item.text)

# user_name = soup.find("div", class_="user__name").find("span").text
#
# find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
#
# for item in find_all_spans_in_user_info:
#     print(item.text)

social_links = soup.find(class_="social__networks").find("ul").find_all("a")
all_a = soup.find_all("a")
# print(social_links)
# print(all_a)
#
# for item in all_a:
#     item_text = item.text
#     item_url = item.get("href")
#     print(f'{item_text}: {item_url}')

post_div = soup.find(class_="post__text").find_parent()
print(post_div.text)
