import threading

class BankAccount(threading.Thread):
    def __init__(self):
        self.balance = 1000
        self.lock = threading.Lock()

    def deposit_Task(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Deposited {amount}, new balance is {self.balance}")

    def withdrew_Task(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}, new balance is {self.balance}")
            else:
                print("Not enough funds to withdraw")

def deposit_task(account, amount):
    for _ in range(5):
        account.deposit_Task(amount)

def withdrew_task(account, amount):
    for _ in range(5):
        account.withdrew_Task(amount)

account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdrew_thread = threading.Thread(target=withdrew_task, args=(account, 150))

deposit_thread.start()
withdrew_thread.start()

deposit_thread.join()
withdrew_thread.join()