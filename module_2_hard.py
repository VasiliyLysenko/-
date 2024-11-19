while 1 > 0:
    n = int(input('Введите число от 3 до 20: '))
    if 3 <= n <= 20:
        break
    else:
        print('Неверное число. Попробуйте еще раз.')

num = []
for i in range(1, n):
    num.append(i)

lst = []
len_ = len(num)

for i in range(len_):
    for j in range(i+1, len_):
        if n % (num[i] + num[j]) == 0:
            lst.append(str(num[i]) + str(num[j]))


print('Пароль:', ''.join(lst))