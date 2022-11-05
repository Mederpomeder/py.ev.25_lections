import json

inf_file = '/home/meder/Desktop/ev.25/files/hackathon/inf.json'
id = 0

def data_():
    with open(inf_file, 'r') as file:
        return json.load(file)

def save(data):
    with open(inf_file, 'w') as file:
        json.dump(data, file)

def id_():
    global id 
    id += 1
    return id

def listing():
    data = data_()
    return f'Список товаров: {data}'

def retrieve():
    data = data_()
    print(listing())
    try:
        id = int(input('Введите id продукта: '))
        product = list(filter(lambda x: id == x['id'], data))
        return product[0]
    except: 
        return 'Неверный id!'  

def create():
    data = data_()
    try:
        product = {
            'id': id_(),
            'mark': input('Введите марку продукта: '),
            'model': input('Введите модель продукта: '),
            'year': int(input('Введите год выпуска: ')),
            'description': input('Введите описание продукта: '),
            'price': round(float(input('Введите цену товара: ')), 2)        
        }  
    except:
        return 'Неверные данные!'

    data.append(product)
    save(data)
    return 'Добавлен новый товар!'

def delete():
    data = data_()
    print(listing())
    try:
        id = int(input('Введите id товара, который надо удалить: '))
        product = list(filter(lambda x: id == x['id'], data))[0]
        print(f'Товар для удаления: {product["mark"]}: {product["model"]}')
    except:
        return 'Неверный id!'

    choice = input('Вы точно хотите удалить товар(yes/no)?: ')
    if choice.lower().strip() != 'yes':
        return 'Товар не удален!'
    data.remove(product)
    save(data)
    return 'Товар удалён!'

def update():
    data = data_()
    print(listing())
    try:
        id = int(input('Введите id продукта: '))
        product = list(filter(lambda x: id == x['id'], data))[0]
        print(f'Товар для обновления {product["mark"]}: {product["model"]}')
    except:
        return 'Неверный id!'

    index = data.index(product)
    choice = input('Что вы хотите изменить (1-марку, 2-модель, 3-год, 4-описание, 5-цену): ')
    if choice.strip() == '1':
        data[index]['mark'] = input('Введите марку: ')
    elif choice.strip() == '2':
        data[index]['model'] = input('Введите модель: ')
    elif choice.strip() == '3':
        try:
            data[index]['year'] == int(input('Введите год выпуска: '))
        except:
            return 'Неверно введён год!'
    elif choice.strip() == '4':
        data[index]['description'] = input('Введите описание: ')
    elif choice.strip() == '5':
        try:
            data[index]['price'] = round(float(input('Введите цену продукта: ')), 2)
        except:
            return 'Неверные данные!'
    else:
        return 'Неверное значение для обновления!'

    save(data)
    return 'Товар обновлён!'

def main():
    choice = input('\n\tСоздать товар - 1\n\tСписок товаров - 2\n\tДетальный обзор - 3\n\tОбновить товар - 4\n\tУдалить товар - 5\nЧто вы хотите сделать: ')
    if choice.strip() == '1':
        print(create())
    elif choice.strip() == '2':
        print(listing())
    elif choice.strip() == '3':
        print(retrieve())
    elif choice.strip() == '4':
        print(update())
    elif choice.strip() == '5':
        print(delete())
    else:
        return 'Неверный выбор!'

    answer = input('Хотите прдолжить(yes/no)?: ')
    if answer.lower().strip() == 'yes':
        main()
    else:
        print('Не люблю прощаться :~(\n\tУдачи!')
main()