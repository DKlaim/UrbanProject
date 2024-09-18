def get_matrix(n, m, value):
    matrix = []  # создали пустой список
    for i in range(n):
        matrix.append([])  # добавили в пустой список n пустых списков
        for _ in range(m):
            matrix[i].append(value)  # в каждый из n списков добавили value m раз
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)