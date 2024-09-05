my_dict = {
    'Alex': 2000,
    'Sasha': 2005,
    'Max': 2010
}
print('Dict:', my_dict)
print('Existing value:', my_dict['Alex'])
print('Not existing value:', my_dict.get('Denis'))

my_dict.update({
    'Denis': 2001,
    'Anton': 2002
})

del_val = my_dict.pop('Denis')
print('Deleted value:', del_val)

print('Modified dictionary:', my_dict)


my_set = {1, 2, 3, 1, 2, 3, 'string', False}
print('Set:', my_set)

my_set.add((1, 2, 3))
my_set.add(4)
my_set.remove(False)
print('Modified set:', my_set)