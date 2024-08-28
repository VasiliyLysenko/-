from threading import Thread
import time
from queue import Queue

class Table:
    def __init__(self, number: int, is_busy: bool):
        self.number = number
        self.is_busy = is_busy

class Cafe:
    def __init__(self, tables: list):
        self.queue_cafe = Queue()
        self.tables = tables
        self.customer_thread = []

    def customer_arrival(self):
        client_number = 1
        while client_number <= 20:
            time.sleep(1)
            print(f'Посетитель номер {client_number} прибыл.')
            self.serve_customer(client_number)
            client_number = client_number + 1

    def serve_customer(self, customer):
        free_table = False
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f'Посетитель {customer} занял столик {table.number}')
                customer_th = Customer(self, customer, self.queue_cafe, table)
                customer_th.start()
                self.customer_thread.append(customer_th)
                free_table = True
                return
        if not free_table:
            print(f'Посетитель {customer} ждет столик')
            self.queue_cafe.put(customer)

class Customer(Thread):
    def __init__(self, cafe, client_number, queue_cafe, table):
        super().__init__()
        self.cafe = cafe
        self.client_number = client_number
        self.queue_cafe = queue_cafe
        self.table = table

    def run(self):
        time.sleep(5)
        print(f'Посетитель {self.client_number} поел и ушел')
        self.table.is_busy = False
        if not self.queue_cafe.empty():
            next = self.queue_cafe.get()
            self.cafe.serve_customer(next)

table1 = Table(1, False)
table2 = Table(2, False)
table3 = Table(3, False)
tables = [table1, table2, table3]

cafe = Cafe(tables)
th1 = Thread(target=cafe.customer_arrival)
th1.start()
th1.join()





