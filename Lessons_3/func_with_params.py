# Параметры со значениями по умолчанию ОБЯЗАТЕЛЬНО должны идти после параметров у которых значения по умолчанию отсутствуют
# Когда мы работаем с параметрами у которых значения по умолчанию, то в качестве этих параметров мы указываем НЕИЗМЕНЯЕМЫЕ ОБЪЕКТЫ

def func_with_params_1(a, b=2, c=[]):  # указан список - изменяемый объект
    c.append(a)
    print(c)


func_with_params_1(3)
func_with_params_1(4)  # каждый новый вызов будет дополнять уже существующий параметр
func_with_params_1(5)
func_with_params_1(6)
print()

def func_with_params_2(a, b=2, c=None):
    if c is None:
        c = []
        c.append(a)
    print(c)


func_with_params_2(3)
func_with_params_2(4)  # каждый новый вызов будет переопределять существующий параметр
func_with_params_2(5)
func_with_params_2(6)