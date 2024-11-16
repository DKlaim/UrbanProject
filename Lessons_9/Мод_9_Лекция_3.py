# Генераторные сборки (всегда записываются как кортеж - в круглых скобках, а также её можно использовать только один раз)
# Пример 1: Ленивые вычисления - когда значение вычисляется при необходимости

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

result = (x ** 100 for x in my_numbers)
print(result)
print()

for elem in result:
    print(elem)
print('Ещё раз')
for elem in result:
    print(elem)

# Пример 2: Генераторные сборки применяются там, где необходимо производить затратные операции
import time

start_time_list = time.time()
result_1 = [x ** 3000 for x in my_numbers]
print(result_1)
for i in result_1:
    print(i)
finish_time_list = time.time()

start_time_gen = time.time()
result_2 = (x ** 3000 for x in my_numbers)
print(result_2)
for i in result_2:
    print(i)
finish_time_gen = time.time()


print(f'Время в миллисекундах при Списковой сборке: {(finish_time_list-start_time_list)*1000}')
print(f'Время в миллисекундах при Генераторной сборке: {(finish_time_gen-start_time_gen)*1000}')


# Пример 3: Встроенные функции с ленивыми вычислениями
list_1 = [1, 2, 3, 4, 5]
list_2 = [9, 8, 7, 6, 5]

rn = range(10, 30)
zp = zip(list_1, list_2)
mp = map(str, list_1)

print(rn, zp, mp)  # на данном этапе функции не производили никаких вычислений

print(list(rn))
print(list(zp))
print(list(mp))