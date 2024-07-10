class Product():
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'
        '''Создает пустой текстовый документ'''
        products = open(self.__file_name, 'a')
        products.close()
        
    def get_products(self):
        file_r = open(self.__file_name, 'r')
        return file_r.read()
        file_r.close()

    def add(self, *products):
        name_products = set()

        '''Формируем множестве имен продуктов'''
        file = open(self.__file_name, 'r')
        for i in file:
            name = i.strip().split(',')[0]
            name_products.add(name)
        file.close()

        '''Добавляем новые продукты если отсутствует имя в множестве имен'''
        file_app = open(self.__file_name, 'a')
        for arg in products:
            if arg.name in name_products:
                print(f'Продукт {arg.name} уже есть в магазине')
            else:
                file_app.write(f'{arg}\n')
                name_products.add(arg.name)
        file_app.close

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)  # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
