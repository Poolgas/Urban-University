'''
Задание "Они все так похожи":
2D? 3D? Даже 4D?.... Настолько глубоко мы заходить конечно же не будем, 4D подождёт, но вот с двумерными и трёхмерными фигурами можем поэкспериментировать.
Вы когда-нибудь задумывались как устроены графические библиотеки для языков программирования?
Безусловно, там выполняются огромные расчёты при помощи вашей видеокарты, но... Что лежит в основе удобного использования таких объектов?

По названию задачи можно понять, что все геометрические фигуры обладают схожими свойствами, такими как: длины сторон, цвет и др.

Давайте попробуем реализовать простейшие классы для некоторых таких фигур и при этом применить наследование (в будущем, изучая сторонние библиотеки, вы будете замечать схожие классы, уже написанные кем-то ранее):

Общее ТЗ:
Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать методами изменения размеров, цвета и т.д.
Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.

Подробное ТЗ:

Атрибуты класса Figure: sides_count = 0
Каждый объект класса Figure должен обладать следующими атрибутами:
Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
Атрибуты(публичные): filled(закрашенный, bool)
И методами:
Метод get_color, возвращает список RGB цветов.
Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
Метод get_sides должен возвращать значение я атрибута __sides.
Метод __len__ должен возвращать периметр фигуры.
Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, то не изменять, в противном случае - менять.

Атрибуты класса Circle: sides_count = 1
Каждый объект класса Circle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).

Атрибуты класса Triangle: sides_count = 3
Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
Атрибуты класса Cube: sides_count = 12
Каждый объект класса Cube должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure.
Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
Метод get_volume, возвращает объём куба.

ВАЖНО!
При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]
'''
from math import pi


class Figure():
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        self.__color = [i for i in color]
        self.filled: bool
        if len(sides) == 1:
            self.__sides = [sides[0] for _ in range(self.sides_count)]
        elif len(sides) != self.sides_count :
            self.__sides = [1 for _ in range(self.sides_count)]
        else:
            self.__sides = [sides[0] for _ in range(self.sides_count)]


    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        if r in range(0, 256) and isinstance(r, int) == True:
            if g in range(0, 256) and isinstance(g, int) == True:
                if b in range(0, 256) and isinstance(b, int) == True:
                    return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) == True:
            self.__color = (r, g, b)

    def __is_valid_sides(self, *new_sides):
        side_check = 0
        for side in new_sides:
            if side > 0 and isinstance(side, int):
                side_check += 1
        if side_check == self.sides_count:
            return True
        else:
            False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides) == True:
            self.__sides = list(new_sides)
        else:
            return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        if len(self.get_sides()) != self.sides_count:
            self._Figure__sides = self.get_sides()[0] * self.sides_count

        self.__radius = (self.get_sides()[0]) / (2 * pi)


    def get_square(self):
        return round(3.14 * (self.__radius ** 2), 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)

    def get_square(self):
        half_perimeter = sum(Figure.get_sides()) / 2
        return (round(half_perimeter * (half_perimeter - self.__sides[0]) * (half_perimeter - self.__sides[1]) * (
                half_perimeter - self.__sides[2]), 2) ** 0.5)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        self._Figure__sides = [self.get_sides()[0] for _ in range(self.sides_count)]

    def get_volume(self):

        return round(self.get_sides()[0] ** 3)


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)


# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
#
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())


# Проверка периметра (круга), это и есть длина:
print(f'Проверка периметра (круга) : {len(circle1)}')

# Проверка объёма (куба):
print(f'Проверка объёма (куба):{cube1.get_volume()}')


# Создание объекта - треугольник
triangle1 = Triangle((200, 200, 100), 10, 7, 14)
print(f'Проверка на изменение сторон трееугольника: \nБыло - {triangle1.get_sides()}')
triangle1.set_sides(17, 3, 14)
print(f'Стало - {triangle1.get_sides()}')

print(f'Провеерка метода вычисляющего площадь треугольника: {circle1.get_square()}')

cube2 = Cube((200, 200, 100), 9)
print(cube2.get_sides())

#Проверки на создание объектов
print(f'Проверка создания круга с одной стороной: {Circle((200, 200, 100), 10).get_sides()}')
print(f'Проверка создания треугольника с одной стороной: {Triangle((200, 200, 100), 10, 6).get_sides()}')
print(f'Проверка создания куба с одной стороной: {Cube((200, 200, 100), 9).get_sides()}')


print(f'Проверка создания круга с двумя сторонами: {Circle((200, 200, 100), 12, 5).get_sides()}')
print(f'Проверка создания треугольника с двумя сторонами: {Triangle((200, 200, 100), 10, 6).get_sides()}')
print(f'Проверка создания куба с тремя сторонами: {Cube((200, 200, 100), 7, 12, 4).get_sides()}')


print(f'Проверка создания треугольника с тремя сторонами: {Triangle((200, 200, 100), 10, 6, 14).get_sides()}')
print(f'Проверка создания куба с двенадцатью разными сторонами : {Cube((200, 200, 100), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12).get_sides()}')
