# Напишите функцию get_multiplied_digits и параметр number в ней.
def get_multiplied_digits(number):

    # Создайте переменную str_number и запишите строковое представление(str) числа number в неё
    str_number = str(number)

    # создайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int)
    first = int(str_number[0])

    # Условия для выполнения всех пунктов
    if 1 < len(str_number):
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

# Вывод на консоль
result = get_multiplied_digits(40203)
print(result)