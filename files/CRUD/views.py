import random 
import json

FILE_PATH = '/home/meder/Desktop/ev.25/files/CRUD/data.json'
ID_FILE_PATH = '/home/meder/Desktop/ev.25/files/CRUD/id.txt'
def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)

def save_data(data):
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file) 
# CRUD 

def list_of_products():
    data = get_data()
    return f'Список всех товаров: {data}'

def detail_product():
    data = get_data()
    try:
        id = int(input('Введиет id продукта: '))
        product = list(filter(lambda x: id == x['id'], data))
        return product[0]
    except: 
        return 'Неверный id!'
            
def get_id():
    with open(ID_FILE_PATH, 'r') as file:
        id = int(file.read())
        id += 1
    with open(ID_FILE_PATH, 'w') as file:
        file.write(str(id))
    return id

def create_product():
    data = get_data()
    try: 
        product = {
            'id': get_id(),
            'title': input('Введите название продукта: '),
            'price': float(input('Введите цену продукта: ')),
            'description': input('Введите описание: ')
        }
    except: 
        return 'Невераные данные!'

    data.append(product)
    save_data(data)
    return 'Создан новый товар!'

# print(create_product())

def update_product():
    data = get_data()
    try:
        id = int(input('Введите id продукта: '))
        product = list(filter(lambda x: id == x['id'], data))[0]
        print(f'Товар для обновления: {product["title"]}')
    except:
        return 'Неверный id!'

    index = data.index(product)
    choice = input('Что вы хотите изменить?(1-title, 2- price, 3-discription): ')
    if choice.strip() == '1':
        data[index]['title'] = input('Введите новое название: ')
    elif choice.strip() == '2':
        try:
            data[index]['price'] = round(float(input('Введите новую цену: ')), 2)
        except:
            return 'Неверное значение для цены!'    
    elif choice.strip() == '3':
        data[index]['description'] = input('Введите новое описание: ')
    else:
        return 'Нверное значение для обновления!'
    
    save_data(data)
    return 'Товар обновлен!'

# print(update_product())

def delete_product():
    data = get_data()
    try:
        id = int(input('Введите id продукта: '))
        product = list(filter(lambda x: id == x['id'], data))[0]
        print(f'Товар для удаления {product["title"]}')
    except:
        return 'Нверный id!'

    choice = input('Удалить этот товар(yes/no)?')
    if choice.lower().strip() != 'yes':
        return 'Товар не удален!'
    data.remove(product)
    save_data(data)
    return 'Товар удалён!'

# print(delete_product())

def main():
    print('Привет! Тебе доступны следующие функции маркет-плейса:\n\tLIST-1:\n\tDETAIL-2:\n\tCREATE-3:\n\tUPDATE-4:\n\tDELETE-5')
    choice = input('Введите действие(1,2,3,4,5): ')
    if choice.strip() == '1':
        print(list_of_products())
    elif choice.strip() == '2':
        print(detail_product())
    elif choice.strip() == '3':
        print(create_product())
    elif choice.strip() == '4':
        print(update_product())
    elif choice.strip() == '5':
        print(delete_product())
    else:
        print('Неверный выбор!')
    
    answer = input('Хотите продолжить(yes/no)?: ')
    if answer.lower().strip() == 'yes':
        main()
    else:
        print('Пока Пока!')

main()