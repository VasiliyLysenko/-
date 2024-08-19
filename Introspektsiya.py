import inspect
def introspection_info(obj):

    obj_type = type(obj).__name__ # Тип объекта

    attributes_ = [attr for attr in dir(obj)] # Находим атрибуты
    methods_ = [method for method in dir(obj)] # Находим методы

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

