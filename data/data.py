import random


class PersonData:
    user_name = 'Ильин Виталий'
    login = 'vvilin@test.ru'
    password = 'V563217233v_'


class ValidData:
    user_name = 'Test test'
    login = f"Test_test{random.randint(10, 999)}@yandex.ru"
    password = f"{random.randint(100, 999)}{random.randint(100, 999)}"
