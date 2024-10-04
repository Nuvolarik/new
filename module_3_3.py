def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
# print_params(a, b) # ошибка
# print_params(a, b, c, d = 4) # ошибка
print_params(b = 25)
print_params(c = [1,2,3])

value_list = [26, 'sign', True]
value_dict = {'a': 98, 'b': 'mentol', 'c': False}

print_params(*value_list)
print_params(**value_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)