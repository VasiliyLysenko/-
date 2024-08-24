import inspect
import sys
def introspection_info(obj):

    obj_type = type(obj).__name__ # Тип объекта

    attributes_ = [attr for attr in dir(obj)] if not callable(getattr(obj, attr)) and not attr.startswith("__")] # Находим атрибуты
    methods_ = [method for method in dir(obj)] if callable(getattr(obj, method)) and not method.startswith("__")] # Находим методы

    module = inspect.getmodule(obj)
    module_name = module.__name__ if module is not None else '__main__' # Находим модуль

    return {
        'type': obj_type,
        'attributes': attributes_,
        'methods': methods_,
        'module': module_name
    }

number_info = introspection_info(42)
print(number_info)

