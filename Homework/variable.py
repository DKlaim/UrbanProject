home_works_count = 12
number_of_hours_spent = 1.5
course_name = 'Python'
time_for_one_task = number_of_hours_spent / home_works_count
print('Курс:', course_name + ', всего задач:', str(home_works_count) + ', затрачено часов:', str(number_of_hours_spent) + ', среднее время выполнения:', time_for_one_task, 'часа.')
print('Курс: ', course_name, ', всего задач: ', home_works_count, ', затрачено часов: ', number_of_hours_spent, ', среднее время выполнения: ', time_for_one_task, ' часа.', sep = '')
print(f'Курс: {course_name}, всего задач: {home_works_count}, затрачено часов: {number_of_hours_spent}, среднее время выполнения: {time_for_one_task} часа.')