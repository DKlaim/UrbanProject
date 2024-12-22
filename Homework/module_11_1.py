import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

HOST = 'https://www.dohod.ru'
URL = 'https://www.dohod.ru/ik/analytics/stockmap'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r.text


def get_securities(html):
    parse = BeautifulSoup(html, 'html.parser')
    securities = []

    for i in range(1, 9):
        products = parse.find_all('td', class_="cc" + f'{i}')
        for product in products:
            securities.append(
                {
                    'Эмитент:': product.find('span', class_="returns-table-cell-title").get_text(),
                    'Стоимость:': product.find('div', class_="returns-table-cell-price").get_text(),
                    'Доходность:': product.find('span', class_="returns-table-cell-return").get_text().rstrip(' %')
                }
            )

    return securities


def save_to_csv(dataset, filename):
    df = pd.DataFrame(dataset)
    df.to_csv(filename, index=False)


def top_securities(filename):
    table = pd.read_csv(filename)
    result = table.sort_values(by=['Доходность:'], ascending=False, ignore_index=True)
    result = result.head(10)
    return result


def main():
    dataset = get_securities(get_html(URL))
    save_to_csv(dataset, 'securities.csv')
    print('--------------')
    for data in dataset:
        for value in data:
            print(value, data[value])
        print('--------------')

    print()
    print('Топ-10 эмитентов по доходности')
    print(top_securities('securities.csv'))

    table = top_securities('securities.csv')
    x = table.values[:, 0]
    y = table.values[:, 2]
    plt.figure(figsize=(13, 5))
    plt.title('Топ-10 эмитентов по доходности')
    plt.bar(x, y)
    plt.show()


if __name__ == '__main__':
    main()
