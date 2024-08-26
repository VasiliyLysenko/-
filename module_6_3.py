class Horse:
    x_distance = 0
    _sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    y_distance = 0
    sound = 'I trean, eat, sleep and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        self._sound = super()._sound
        self.sound = super().sound

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        pos_pegasa = (self.x_distance, self.y_distance)
        return pos_pegasa

    def voice(self):
        print(self.sound)


p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()