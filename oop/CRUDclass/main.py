def search_object(func):
    def wrapper(*args, **kwargs):
        self = args[0]
        id = args[1]
        for obj in self.objects:
            if obj['id'] == id:
                kwargs.update(object_ =obj)
                return func(*args, **kwargs)
        kwargs.update(object_=None)
        return func(*args, **kwargs)
    return wrapper 

class Car:
    def _get_or_set_objects_and_id(self):
        try:
            if (self.objects or not self.objects) and (self.id or not self.id):
                pass 
        except (NameError, AttributeError):
            self.objects = []
            self.id = 0

    def __init__(self) -> None:
        self._get_or_set_objects_and_id()

    def save(self):
        import json
        with open('/home/meder/Desktop/ev.25/oop/CRUDclass/airtable.json', 'w') as file:
            json.dump(self.objects, file)
        return 'Saved!'

    def create(self, **kwargs):
        self.id += 1
        object_ = dict(id=self.id, **kwargs)
        self.objects.append(object_)
        self.save()
        print(f'status: 201, msg: {object_}')

    def list(self):
        res = []
        for obj in self.objects:
            res.append({'id': obj['id'] ,'mark': obj['mark'], 'model' : obj['model'], 'year' : obj['year'], 'engine_volume' : obj['engine_volume'], 'color' : obj['color'], 'body_type' : obj['body_type'], 'mileage': obj['mileage'], 'price': obj['price']})
        print(f'status: 200, msg: {res}')

    @search_object
    def detail(self, id, **kwargs):
        obj = kwargs['object_']
        if obj:
            print(f'status: 200, msg: {obj}')
        else:
            print('status: 404, msg: Not found!')

    @search_object
    def update(self, id, key, **kwargs):
        obj = kwargs.pop('object_')
        if obj:
            try:
                if obj[key]:
                    obj[key] = input('Новое значение: ')
                    obj.update(**kwargs)
                    self.save()
                    print(f'status: 206, msg: {obj}')
            except:
                print('status: 404, msg: Not Found!')
        else:
            print('status: 404, msg: Not found!')

    @search_object
    def delete(self, id, **kwargs):
            obj = kwargs.get('object_')
            if obj:
                self.objects.remove(obj)
                self.save()
                print('status: 204, msg: Deleted!')
            else:
                print('status: 404, msg: Not found!')

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
    with open('cars.csv', 'a') as file:
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
    with Pool(40) as pool:
        pool.map(make_all, links)
    finish = datetime.now()
    print(f'Парсинг занял: {finish - start}')

main()












test = Car()
test.create(mark='BMW', model= 'x7', year= 2020, engine_volume= 12, color= 'red', body_type= 'SUV', mileage= 200, price= 505)
test.create(mark= 'BMW', model= 'x5', year= 2022, engine_volume= 16, color= 'blue', body_type= 'pickuo', mileage= 300, price= 400)
test.create(mark= 'BMW', model= 'x4', year= 2016, engine_volume= 8, color= 'black', body_type= 'coupe', mileage= 150, price= 609)
test.list()
test.detail(1)
test.update(1, 'price')
test.delete(2)
