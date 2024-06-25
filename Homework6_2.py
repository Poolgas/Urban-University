class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = str(owner)
        self.model = str(__model)
        self.engine_power = int(__engine_power)
        self.color = str(__color)

    def get_model(self):
        print(f'Модель: {self.model} ')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.engine_power} ')

    def get_color(self):
        print(f'Цвет: {self.color}')

    def get_owner(self):
        print(f'Владелец: {self.owner}')

    def print_info(self):
        self.get_model(), self.get_horsepower(), self.get_color(), self.get_owner()

    def set_color(self, new_color):
        self.n_color = str(new_color)
        if self.n_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.color = self.n_color

        else:
            print(f'Невозможно покрасить в {self.n_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
