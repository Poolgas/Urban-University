class Building:
    def __init__(self, buildingType, numberOfFloors):
        self.buildingType = buildingType
        self.numberOfFloors = numberOfFloors


    def __int__(self):
        return f'{self.numberOfFloors}'

    def __str__(self):
        return f'{self.buildingType}'

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


h1 = Building('Skyscaper', 5)
h2 = Building('Town_House', 2)

print(h1 == h2)