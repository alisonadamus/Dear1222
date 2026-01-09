import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/blogs/"

# Ідентифікуємося як звичайний користувач (щоб сайт не заблокував)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")

    menu = soup.find("ul", class_="list-recent-posts menu")
    menu_items = menu.find("li")

    for item in menu_items:
        name = item.find("a")

else:
    print("Не вдалося завантажити сторінку:", response.status_code)
