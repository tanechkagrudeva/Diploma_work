from utils import import_csv_data, find_price
from pathlib import Path
from classes import Product

menu_exit = True

while menu_exit:
    print("Здравствуйте! Напишите полный путь к файлу с данными(ВАЖНО! файл в формате .csv)")
    print("Для выхода из программы напишите 'exit'")
    user_csv = input()
    if user_csv.lower() == 'exit':
        menu_exit = False
        break
    if user_csv.endswith('csv') is False:
        print('Путь указан неверно')
    else:
        count_sales = input('Введите какое min количество продаж учитывается ')
        # Если пользователь ничего не укажет, по умолчанию будет 10
        if count_sales.isdigit() is False:
            count_sales = 10
        user_csv.replace("\\", "/")
        user_csv = str(Path(user_csv))
        needed_price = find_price(import_csv_data(user_csv, count_sales))
        print("Результат:")
        for i in needed_price:
            product = Product(i[0], i[1])
            print(product)

        print("Хотите продолжить работу? (пишите 'да' или 'нет')")
        answer = input()
        if answer.lower() == 'нет':
            menu_exit = False