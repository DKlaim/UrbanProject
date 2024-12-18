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

    # items = parse.find_all('div', class_="tabs")
    # items = parse.find_all('table', class_="returns-table")
    # items = parse.find_all('tbody', id="micexindexcf_shares")
    items = parse.find_all('td', class_="cc1")
    for item in items:
        securities.append(
            {
                'title': item.find('span', class_="returns-table-cell-title").get_text(),
                'price': item.find('div', class_="returns-table-cell-price").get_text(),
                'return': item.find('span', class_="returns-table-cell-return").get_text()
            }
        )

    items = parse.find_all('td', class_="cc8")
    for item in items:
        securities.append(
            {
                'title': item.find('span', class_="returns-table-cell-title").get_text(),
                'price': item.find('div', class_="returns-table-cell-price").get_text(),
                'return': item.find('span', class_="returns-table-cell-return").get_text()
            }
        )

    return securities


def main():
    data = get_data(get_html(URL))
    for data in data:
        print(data)


if __name__ == '__main__':
    main()
