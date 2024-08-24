import inspect
import sys


def introspection_info(obj):
    # Определяем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты и методы объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods = [method for method in dir(obj)]

    # Получаем модуль, к которому принадлежит объект
    module = inspect.getmodule(obj)
    module_name = module.__name__ if module is not None else '__main__'

    # Возвращаем собранную информацию в виде словаря
    return {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module_name
    }


# Пример использования функции
number_info = introspection_info(42)
print(number_info)
