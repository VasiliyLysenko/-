import threading
import queue
from time import sleep


class Table: # класс для столов

    tables = []

    def __init__(self, number, is_busy, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number = number

    def bool(self):
        for i in range(self.number):
            i += 1
            Table.tables.append(i)


class Cafe: # класс для симуляции процессов в кафе
    visitors = []

    def __init__(self, queue, *args, **kwargs):
        self.queue = queue # очередь посетителей

    def customer_arrival(self): # моделирует приход посетителя(каждую секунду)


    def serve_customer(self, customer): # моделирует обслуживание посетителя. Время обслуживания 5 секунд.

class Customer: # Запускается, если есть свободные столы
