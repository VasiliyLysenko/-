from threading import Thread
from time import sleep, time

def wite_words(word_count, file_name):
        with open(file_name, 'a', encoding='utf-8') as f: # открываем файл в режиме добавления
                for i in range(1, word_count + 1):
                        f.write(f'Какое-то слово № {i}\n')
                        sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

start_time = time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
end_time = time()
print(f'Общее время работы функции {end_time - start_time:.2f} секунд(ы)')

print('---------------')

start_time = time()
t1 = Thread(target=wite_words, args=(10, 'example5.txt',))
t2 = Thread(target=wite_words, args=(30, 'example6.txt',))
t3 = Thread(target=wite_words, args=(200, 'example7.txt',))
t4 = Thread(target=wite_words, args=(100, 'example8.txt',))

t1.start() # можно прописать циклом
t2.start()
t3.start()
t4.start()

t1.join() # можно прописать циклом
t2.join()
t3.join()
t4.join()

end_time = time()
print(f'Время работы потоков {end_time - start_time:.2f} секунд(ы)')