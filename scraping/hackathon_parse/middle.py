from bs4 import BeautifulSoup
import requests
import csv
from multiprocessing import Pool
from datetime import datetime

count = 0

def get_html(url):
    response = requests.get(url)
    return response.text

def get_cars_links(html):
    urls = []
    soup = BeautifulSoup(html, 'lxml')
    catalog = soup.find('div', class_='listing search-page x-3')
    items = catalog.find_all('div', class_='listing-item main')
    for item in items:
        a = item.find('a').get('href')
        link = 'https://www.mashina.kg' + a
        urls.append(link)
    return urls
    
def get_all_links():
            
    links = []
    for i in range(1, 5):
        url = f'https://www.mashina.kg/new/search?page={i}'
        html = get_html(url)
        cars_links = get_cars_links(html)
        links.extend(cars_links)
    return links

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    
    catalog = soup.find('div', class_='page-content')
    if not catalog:
        False
    
    title = catalog.find('h1').text.strip()
    description = catalog.find('div', class_='left')
    names = (x.text for x in description.find_all('span', class_='name'))
    values = (y.text for y in description.find_all('span', class_='value'))
    desc = {x: y for x, y in zip(names, values)}
    
    
    price = catalog.find('span', class_='main').text.strip()
    try:   
        image = catalog.find('div', class_="main-image").find('img').get('data-src')
    except:
        image= 'Нет картинки!'
    data = {
        'title': title,
        'price': price,
        'img': image,
        'description': desc
    }
    return data

def write_csv(data):
    with open('mashina.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['title'], data['price'], data['img'], data['description']))
        print(f'{data["title"]} - парсятся!')


def prepare_csv():
    global count
    with open('mashina.csv', 'w') as file:
        fieldnames = ['Марка', "Цена", "Фото", "Описание"]
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            'Марка': 'Марка',
            'Цена': 'Цена',
            'Фото': 'Фото',
            'Описание': 'Описание'
        })  

def make_all(link):
    data = get_html(link)
    res = get_data(data)
    write_csv(res)

def main():
    prepare_csv()
    links = get_all_links()
    start = datetime.now()
    with Pool(40) as pool: # параллельно
        pool.map(make_all, links)
    finish = datetime.now()
    print(f'Парсинг занял: {finish - start}')
    #map(make_all, links)
    # for link in links:
    #     data = get_html(link)
    #     res = get_data(data)
    #     write_csv(res)

main()







