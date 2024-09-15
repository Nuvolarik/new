my_dict = {'Liam': 1952, 'Sylvester': 1946, 'Jackie': 1954}
print(my_dict)

print(my_dict['Jackie'])
my_dict['Keanu'] = 1964
print(my_dict['Keanu'])

my_dict.update({'Bruce': 1955,
                'Chuck': 1940})

del my_dict['Sylvester']
print(my_dict.get('Sylvester'))

print(my_dict)
print('__________')

my_set = {'гвоздь', '44', 'брусок', '15', '78', 'шуруп', '44','гвоздь', 'замок', '61', 'кирпич', 'шуруп', '15'}
print(my_set)

my_set.add(49)
my_set.add('молоток')
my_set.remove('гвоздь')
print(my_set)