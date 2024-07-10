# Работа со словарями:

my_dict = {'Василий': 1993, 'Наталья': 1994}
print(my_dict)
print(my_dict['Наталья']) # Значение по существующему ключу
print(my_dict.get('Вовка')) # Значение не по существующему ключу
print(my_dict)

# Добавляем еще две пары в словарь и удалим одну пару
my_dict.update({'Елена': 1972,
                'Владимир': 1968})
print(my_dict)
print(my_dict.pop('Василий'))
print(my_dict)
print('---------------')

# Работа со множествами
my_set = {1, 2, 3, 4, 1, 2, 3, 4}
print(my_set)

# Добавляем два значения и удалем одно
my_set.add(5)
my_set.add(6)
print(my_set)
my_set.discard(1)
print(my_set)