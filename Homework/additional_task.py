# Вводные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_student_score = {}

# Сортируем список студентов в алфавитном порядке
students = list(students)
students.sort()

# Создаём словать со средним балом для каждого студента
for i in range(len(students)):
    average_student_score[students[i]] = sum(grades[i]) / len(grades[i])

# Вывод словаря
print(average_student_score)