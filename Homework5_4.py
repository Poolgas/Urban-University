class Building:
    name: str = None
    total = 0

    def __init__(self, n_build: str):
        self.n_build = n_build
        Building.total += 1

    def __str__(self):
        return "Строение: " + self.n_build

    __repr__ = __str__


build = [Building(f"Build_{i}") for i in range(1, 41)]
for i in range(1, 41):
    print(f'Объект_{i}:', build[i - 1])
