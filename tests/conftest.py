import pytest
import os
from utils import import_csv_data
from classes import Product

data = os.path.join('csv_data_110_.csv')


@pytest.fixture
def item_test():
    data = os.path.join('tests', 'csv_data_110.csv')
    x = import_csv_data(data, 15)
    return x


@pytest.fixture
def item_test2():
    return [['product1', 57957], ['product6', 61774], ['product4', 39249], ['product8', 52434], ['product3', 71536],
            ['product5', 43801], ['product11', 68456], ['product2', 22600], ['self', 63850], ['product10', 64975],
            ['product9', 75156], ['product7', 73667]]


@pytest.fixture
def item_test3():
    x = Product('df', 15)
    return x