import csv
from errors import InstantiateCSVError


def import_csv_data(csv_data, count_):
    """ Функция принимает csv файл с данными и преобразует в оформленный список словарей, где ключом
    будет название продукта, а значения суммой цен и их кол-вом. Count_ необходим для настройки
     какого количества продаж не достаточно, чтобы учитывать цену в статистику"""
    try:
        with open(csv_data, encoding='utf-8') as r_file:
            names_product = []
            price_id = 0
            count_id = 0
            product_id = 0
            """Создаем объект reader, указываем символ-разделитель ","""""
            file_reader = csv.reader(r_file, delimiter=",")
            """ Считывание данных из CSV файла """
            for row in file_reader:
                need_key = False
                if len(names_product) == 0:
                    for i in range(len(row)):
                        if row[i] == 'price':
                            price_id = i
                        if row[i] == 'count':
                            count_id = i
                        if row[i] == 'product':
                            product_id = i
                # проверка, если первая строчка с шапкой названий или неверно заполненные данные
                # больше good_ убирает маленькое кол-во продаж
                if row[price_id].isdigit() and row[count_id].isdigit() and (int(row[count_id]) >= int(count_)):
                    if len(names_product) != 0:
                        for i in names_product:
                            for k, v in i.items():
                                if k == row[product_id]:
                                    v[0] = v[0] + int(row[price_id])
                                    v[1] += 1
                                    need_key = True

                    if (len(names_product) == 0) or (need_key is False):
                        data = {f'{row[product_id]}': [int(row[price_id]), 1]}
                        names_product.append(data)

                else:
                    continue
            return names_product
    except FileNotFoundError:
        print("По указанному пути файл отсутствует")

    except InstantiateCSVError:
        print("Файл поврежден")


def find_price(data):
    clear_list = []
    for i in data:
        for k, v in i.items():
            price = int(v[0]) / int(v[1])
            clear_list.append([k, int(price)])

    return clear_list
