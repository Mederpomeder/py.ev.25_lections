from views import list_of_products, detail_product, create_product, update_product, delete_product

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