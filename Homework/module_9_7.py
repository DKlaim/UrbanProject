def is_prime(func):
    def wrapper(*args):

        number = func(*args)

        is_prime = True
        for n in range(2, number):
            if number % n == 0:
                is_prime = False
                break
        if is_prime:
            print('Простое')
            return number
        else:
            print('Составное')
            return number

    return wrapper


@is_prime
def sum_three(a: int, b: int, c: int):
    result = a + b + c
    return result


result = sum_three(2, 3, 6)
print(result)
