from time import sleep
from threading import Thread
from collections import defaultdict

class Knight(Thread):

    def __init__(self, name, skills, warriors, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skills = skills
        self.warriors = warriors

    def run(self):
        print(f"{self.name}, на нас напали!")

        for skills in range(0, self.warriors, self.skills):
            self.warriors -= self.skills
            sleep(0.1)
            print(f"{self.name}, сражается {int(skills / self.skills) + 1} день(дня)..., осталось {self.warriors} воинов")
        if self.warriors <= 0:
            print(f"{self.name} одержал победу спустя {int(skills / self.skills) + 1} дней")

knight1 = Knight("Sir Lancelot", 10, 100 )  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20, 100 )  # Высокий уровень умения

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print("Все битвы закончились!")