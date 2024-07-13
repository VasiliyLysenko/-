numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] # Список содержащий простые числа
not_primes = [] # Список содержащий непростые числа
is_prime = 0

for i in numbers:
    for j in range(1, i + 1):
        if i % j == 0:
            is_prime += 1
    if is_prime == 2:
        primes.append(i)
        is_prime = 0
    else:
        not_primes.append(i)
        is_prime = 0

print(primes)
print(not_primes)

