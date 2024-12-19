import requests
from bs4 import BeautifulSoup

HOST = 'https://www.dohod.ru'
URL = 'https://www.dohod.ru/ik/analytics/stockmap'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r.text


def get_data(html):
    parse = BeautifulSoup(html, 'html.parser')
    securities = []

    for i in range(1, 9):
        items = parse.find_all('td', class_="cc" + f'{i}')
        for item in items:
            securities.append(
                {
                    'Эмитент:': item.find('span', class_="returns-table-cell-title").get_text(),
                    'Стоимость:': item.find('div', class_="returns-table-cell-price").get_text(),
                    'Доходность:': item.find('span', class_="returns-table-cell-return").get_text()
                }
            )

    return securities


def main():
    datas = get_data(get_html(URL))
    print('--------------')
    for data in datas:
        for value in data:
            print(value, data[value])
        print('--------------')


if __name__ == '__main__':
    main()
