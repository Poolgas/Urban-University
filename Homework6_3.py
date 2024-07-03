class Horse():
    def __init__(self, x_distance=0, sound='Frrr'):
        super().__init__()
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):
        self.dx = dx
        self.x_distance += self.dx
        return self.x_distance


class Eagle():
    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        super().__init__()
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.dy = dy
        self.y_distance += self.dy
        return self.y_distance

    def __str__(self):
        return self.sound

class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(Eagle(self.sound))

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
