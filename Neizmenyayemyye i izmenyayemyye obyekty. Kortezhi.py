# Создание переменной и кортежа в ней

immutable_var = 1, True, 'string'
print(immutable_var)

# Изменение значений переменных:

immutable_var[0] = 200
print(immutable_var) # Кортежи не поддерживают обращение по элементам, если внутри кортежа не список.

# Создание изменяемых структур данных:

mutable_list = ['coconut', 1, True, 5.5]
print(mutable_list)
mutable_list[0] = 'banana' # изменяем элемент
mutable_list.append('Modified') # добавлем элемент
print(mutable_list)
