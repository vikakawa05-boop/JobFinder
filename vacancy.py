import requests
from bs4 import BeautifulSoup

from config import HEADERS


def parse_vacancy(url):

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=30
    )

    soup = BeautifulSoup(response.text, "lxml")

    vacancy = {
        "title": "",
        "company": "",
        "salary": "",
        "experience": "",
        "description": "",
        "url": url
    }

    # Название вакансии
    h1 = soup.find("h1")
    if h1:
        vacancy["title"] = h1.get_text(strip=True)

    # Берем описание из meta
    meta = soup.find("meta", attrs={"name": "description"})
    if meta:
        text = meta.get("content", "")
        vacancy["description"] = text

        # Компания
        if "в компании" in text:
            company = text.split("в компании")[1].split(".")[0].strip()
            vacancy["company"] = company

        # Зарплата
        if "Зарплата:" in text:
            salary = text.split("Зарплата:")[1].split(".")[0].strip()
            vacancy["salary"] = salary

        # Опыт
        if "Требуемый опыт:" in text:
            experience = text.split("Требуемый опыт:")[1].split(".")[0].strip()
            vacancy["experience"] = experience

    return vacancy