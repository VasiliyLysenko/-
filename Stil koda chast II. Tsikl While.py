# Создаем переменную для списка и переменную для начального значения перебора по индексам

my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0

# Пишем цикл

while i < len(my_list):
    if my_list[i] > 0:
        print(my_list[i])
        i += 1
    elif my_list[i] == 0:
        i += 1
        continue
    else:
        if my_list[i] < 0:
            break



