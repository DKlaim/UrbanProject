from multiprocessing import Pool
import time


def read_info(name):
    all_data = []
    with open(name, encoding='utf-8') as file:
        while file.readline() != '':
            all_data += file.readline()


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# # Линейный вызов
# time_start = time.time()
#
# for filename in filenames:
#     read_info(filename)
#
# time_stop = time.time()
# print(time_stop - time_start)


# Многопроцессный
if __name__ == '__main__':
    with Pool() as p:
        time_start = time.time()
        p.map(read_info, filenames)
        time_stop = time.time()
        print(time_stop - time_start)
