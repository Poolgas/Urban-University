class House():
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f'Number of floors: {self.numberOfFloors}')

h1 = House()
print(h1.numberOfFloors)
h1.setNewNumberOfFloors(5)
