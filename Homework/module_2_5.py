def get_matriX(n, m, value):
    matriX = []
    for i in range(n):
        matriX.append([])
        for j in range(m):
            matriX[i].append(value)
    return matriX

result1 = get_matriX(2, 2, 10)
result2 = get_matriX(3, 5, 42)
result3 = get_matriX(4, 2, 13)

print(result1)
print(result2)
print(result3)