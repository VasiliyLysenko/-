def add_everything_up(a, b):
    try:
        res = a + b
        return round(res, 3)
    except TypeError:
        a = str(a)
        b = str(b)
        res = a + b
        return res


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))