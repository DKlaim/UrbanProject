import threading

# Проблемы многопоточного программирования, блокировки и обработка ошибок внутри потоков
counter = 0
lock = threading.Lock()  # переменная блокировки/деблокировки потоков для их синхронизации


def increment(name):
    global counter
    lock.acquire()  # установка блокировки
    for i in range(1000):
        counter += 1
        print(name, counter, lock.locked())  # locked показывает, стоит блокировка или нет
    lock.release()  # снятие блокировки


def decrement(name):
    global counter
    with lock:  # более компактная запись блокировки (всё что в теле оператора with будет выполняться с блокировкой)
        for i in range(1000):
            counter -= 1
            print(name, counter, lock.locked())


# Пример тестирования какого-то блока кода с блокировкой (необходимо для контроля процесса при работе с общими данными)
def decrement2(name):
    global counter
    try:
        lock.acquire()  # ставим блокировку
        for i in range(1000):
            counter -= 1
            print(name, counter, lock.locked())
    except Exception:
        pass
    finally:
        lock.release()  # снимаем блокировку


thread_1 = threading.Thread(target=increment, args=('thread_1',))
thread_2 = threading.Thread(target=decrement, args=('thread_2',))
thread_3 = threading.Thread(target=increment, args=('thread_3',))
thread_4 = threading.Thread(target=decrement, args=('thread_4',))

thread_1.start()
thread_3.start()
thread_2.start()
thread_4.start()
