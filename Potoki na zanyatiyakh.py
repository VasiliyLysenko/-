from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super(Knight, self).__init__()
        self.name = name
        self.power = power
        self.warriors = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        days = 0

        while self.warriors > 0:
            days += 1
            sleep(1)
            self.warriors -= self.power
            if self.warriors < 0:
                self.warriors = 0
            print(f'{self.name} сражается {days}..., осталось {self.warriors} воинов.')

        print(f'{self.name} одержал победу спустя {days} дней(дня)!')

first_thread = Knight('Sir Lancelot', 10)
second_thread = Knight('Sir Galahad', 20)

first_thread.start()
second_thread.start()

first_thread.join()
first_thread.join()

print('Все битвы закончились')







