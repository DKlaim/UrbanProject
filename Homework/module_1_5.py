immutable_var = 1, 2.5, 'string', True
print('Immutable tuple:', immutable_var)

# immutable_var[0] = 0 # будет ошибка, т.к. кортеж не поддерживает изменение своих элементов, это неизменяемый список

mutable_list = list(immutable_var)
mutable_list.append('Modified')
print('Mutable list:', mutable_list)