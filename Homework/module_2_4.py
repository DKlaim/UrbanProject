# Дано
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Найти
primes = []
not_primes = []

# for i in numbers:
#     if i == 1:
#         continue
#     else:
#         for j in numbers:
#             if j == 1:
#                 continue
#             else:
#                 if i % j == 0 and i == j:
#                     primes.append(i)
#                     break
#                 elif i % j == 0 and j < i:
#                     not_primes.append(i)
#                     break
#                 else:
#                    continue



for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)


print(primes)
print(not_primes)