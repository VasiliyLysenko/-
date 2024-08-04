import threading

class BankAccount(threading.Thread):
    def __init__(self):
        self.balance = 1000
        self.Lock = threading.Lock()

    def Deposit_Task(self, amount):
        with self.Lock:
            self.balance += amount
            print(f'Deposited {amount}, new balance is {self.balance}')

    def Withdrew_Task(self, amount):
        with self.Lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f'Withdrew {amount}, new balance is {self.balance}')
            else:
                print('"Not enough funds to withdraw"')


def deposit_task(account, amount):
  for _ in range(5):
    account.Deposit_Task(amount)

def withdraw_task(account, amount):
  for _ in range(5):
    account.Withdrew_Task(amount)

account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()