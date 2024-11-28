import threading
from time import sleep, time


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for n in range(1, word_count + 1):
            file.write(f'Какое-то слово № {n}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
fin = time()

elapsed = round(fin - start, 4)
print(f'Функции завершили свою работу за {elapsed} секунд(ы)')

flow_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
flow_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
flow_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
flow_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

start = time()
flow_1.start()
flow_2.start()
flow_3.start()
flow_4.start()
flow_1.join()
flow_2.join()
flow_3.join()
flow_4.join()
fin = time()

elapsed = round(fin - start, 4)
print(f'Потоки завершили свою работу за {elapsed} секунд(ы)')