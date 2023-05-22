import requests
from bs4 import BeautifulSoup

URL = 'https://auto.drom.ru/region55/mitsubishi/all/'

def get_html(url):
    r = requests.get(url)
    return r.text

def get_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', {'class': "css-xb5nz8 e1huvdhj1"})

    cars = []
    for item in items:
        cars.append({
            'title': item.find('span', {'data-ftid': 'bull_title'}).get_text(),
            'description': item.find('div', {'data-ftid': 'component_inline-bull-description'}).get_text(),
            'price': item.find('span', {'data-ftid': 'bull_price'}).text
        })

    return cars

def parse():
    html = get_html(URL)
    if html:
        cars = get_info(html)
        with open('output.txt', 'w') as f:
            for car in cars:
                f.write(car['title'] + '\n')
                f.write(car['description'] + '\n')
                f.write(car['price'] + '\n\n')
    else:
        print('ERROR')

parse()