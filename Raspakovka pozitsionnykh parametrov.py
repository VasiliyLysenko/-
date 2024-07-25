# Создаем функцию с 3 параметрами

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(2, 'строковое значение', False) # Значения другие
print_params() # Вызов функции без аргуентов
# print_params(1, 2, 3, 4) # Выйдет ошибка, т.к. должно быть столько же аргументов как и в шапке функции
print_params(b=25, c=[1, 2, 3]) # Все замечательно работает

print('-------------------------')

# Создаем список и словарь с разными типами элементов

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [5, 'Машина', True]
values_dict = {'a': 2, 'b': 'string', 'c': False}

print_params(*values_list) # Распаковка списка
print_params(**values_dict) # Распаковка словаря

# Распаковка + отдельные параметры

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42) # Все замечательно работает

