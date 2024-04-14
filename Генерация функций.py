def function_factory(operation): # Создание Фабрики функций
    if operation == "multiplication":
        def multiplication(x, y):
            return x * y
        return multiplication
    elif operation == "division":
        def division(x, y):
            return x / y
        return division

func = function_factory("multiplication")
print(func(2, 3))
func = function_factory("division")
print(func(2, 1))
# func = function_factory("division") # Здесь будет выдаваться ошибка
# print(func(2, 0))

# Создание лямбда функции
multiplication = lambda x, y: x ** y
print(multiplication(2, 3))

def exponentiation(x, y):
    return x ** y
print(exponentiation(3, 3))

# Вызываемые Объекты
class Rect:
    def __init__(self,a, b):
        self.a = a
        self.b = b
    def __call__(self, a, b):
        return a * b

rect = Rect(2, 4)
print(rect.__call__(2, 4))



