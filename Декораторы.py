def is_prime(sum_three):
    def wrapper(*args):
        result = sum_three(*args)
        if result < 2:
            print("Не простое")
        elif result == 2:
            print("Простое")
        elif result % 2 == 0:
            print("Составное")
        else:
            for i in range(2, int(result ** 0.5 + 1), 3):
                if result % i == 0:
                    print("Составное")
                else:
                    print("Простое")

        return result

    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)





