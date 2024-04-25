from time import sleep
from threading import Thread

def func1():
    for i in range(1, 11):
        print(f"{i}", flush=True)
        sleep(1)

def func2():
    text = "abcdefghij"
    for symbol in text:
        print(symbol, flush=True)
        sleep(1)

thread1 = Thread(target=func1)
thread2 = Thread(target=func2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()




