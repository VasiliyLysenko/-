numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] # Список содержащий простые числа
not_primes = [] # Список содержащий непростые числа
is_prime = True
divider = 0

for i in numbers:
    if i == 1:
        continue
    for j in range(1, i + 1):
        if i % j == 0:
            divider += 1
    if divider == 2:
        is_prime = True
        primes.append(i)
        divider = 0
    else:
        is_prime = False
        not_primes.append(i)
        divider = 0

print(primes)
print(not_primes)
