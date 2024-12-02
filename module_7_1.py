class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        prod_list = products
        for i in prod_list:
            file_a = open(self.__file_name, 'a')
            file_text = self.get_products()
            if i.name in file_text:
                print(f'Продукт {i.name} уже есть в магазине')
                file_a.close()
            else:
                file_a.write(f'{str(i)}\n')
                file_a.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())