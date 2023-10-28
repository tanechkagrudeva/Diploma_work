from utils import import_csv_data, find_price


def test_get_file_not_found_error():
    "Test исключения FileNotFoundError в связи с отсутствием файла"""
    assert import_csv_data('tyr.csv', 10) == print("По указанному пути файл отсутствует")


def test_instantiateCSVError():
    "Test исключения FileNotFoundError в связи с отсутствием файла"""
    assert import_csv_data('csv_data_bad.csv', 10) == print("Файл поврежден")


def test_find_price(item_test2, item_test):
    assert find_price(item_test) == item_test2


# def test_import_csv_data(item_test):
#     assert type(item_test) == type([])


def test_import_csv_data(item_test):
    assert isinstance(type(item_test), list) is not True


def test_class_product(item_test3):
    assert item_test3.name == 'df'
    assert item_test3.price == 15