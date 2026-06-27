from search import get_links
from vacancy import parse_vacancy


def main():

    print("=" * 50)
    print("JOB FINDER")
    print("=" * 50)

    links = get_links()

    print(f"\nВсего найдено вакансий: {len(links)}\n")

    for i, link in enumerate(links, start=1):

        print("=" * 50)
        print(f"Вакансия №{i}")
        print("=" * 50)

        vacancy = parse_vacancy(link)

        print("Название :", vacancy["title"])
        print("Компания :", vacancy["company"])
        print("Зарплата :", vacancy["salary"])
        print("Опыт     :", vacancy["experience"])
        print("Ссылка   :", vacancy["url"])


if __name__ == "__main__":
    main()