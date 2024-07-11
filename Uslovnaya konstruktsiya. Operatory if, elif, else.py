# Создаем переменные для ввода с клавиатуры
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

# Пишем условия для каждого случая
if first == second and second == third and third == first:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    if first != second and second != third and third != first:
        print(0)