from math import sqrt


def is_prime(func):
    def prime_or_not(first_int, second_int, third_int):
        result = func(first_int, second_int, third_int)
        square_root = round(sqrt(result))
        for i in range(2, square_root + 1):
            if not result % i:
                return f'Составное\n{result}'
        return f'Простое\n{result}'
    return prime_or_not


@is_prime
def sum_three(first_int, second_int, third_int):
    res = first_int + second_int + third_int
    return res


result = sum_three(2, 3, 6)
print(result)