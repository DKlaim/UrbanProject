def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        if isinstance(a, int) or isinstance(a, float):
            a = str(a)
            return a + b
        elif isinstance(b, int) or isinstance(b, float):
            b = str(b)
            return a + b


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
