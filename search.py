import requests
from bs4 import BeautifulSoup

from config import SEARCH_QUERIES, HEADERS, MAX_VACANCIES


def get_links():

    all_links = []

    for query in SEARCH_QUERIES:

        print(f"\nИщу: {query}")

        url = (
            "https://hh.ru/search/vacancy"
            f"?text={query.replace(' ', '+')}"
        )

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=30
        )

        soup = BeautifulSoup(response.text, "lxml")

        for a in soup.find_all("a", href=True):

            href = a["href"]

            if "/vacancy/" not in href:
                continue

            if "/search/" in href:
                continue

            if href.startswith("/"):
                href = "https://hh.ru" + href

            href = href.split("?")[0]

            if href not in all_links:
                all_links.append(href)

        print("Найдено:", len(all_links))

    return all_links[:MAX_VACANCIES]