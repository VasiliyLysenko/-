# Переменная вне функций
calls = 0

def count_calls(): # подсчитывающая вызовы остальных функций
    global calls
    calls += 1

def string_info(string_1): # принимает аргумент - строку и возвращает кортеж
    count_calls()
    print()
    return (len(string_1), string_1.upper(), string_1.lower()) # Возвращает значения длины, верхнего и нижнего регистра строки

def is_contains(string_2, list_to_search): # принимает два аргумента: строку и список
    count_calls()
    if string_2.lower() in list_to_search: # приводим искомую строку и все строки в списке в один регистр
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'banan', 'urban']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
