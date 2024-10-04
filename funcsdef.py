def print_params(*params): # *args, **kwargs
    print(params)

print_params(1,2,3,4,5,6,7) # упаковались в кортеж

print('----1----')

def print_params(*params): # *args, **kwargs
    print(*params)

print_params(1,2,3,4,5,6,7) # распоковались из кортежа

print('----2----')

def print_params(a, b, c):
    print(a, b, c)

list_ = [1, 2, 3]
print_params(list_, 2, 3) # без звездочки надо передавать 3 значения как в начале функции

print('----3----')

def print_params(a, b, c):
    print(a, b, c)

list_ = [1, 2, 3]
print_params(*list_) # со звездочкой распаковывает список сразу

print('----4----')

def print_params(a, b, c):
    print(a, b, c)

dict_ = {'a': 1, 'b': 2, 'c': 3}
print_params(**dict_)

print('----5----')

def print_params(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

dict_ = {'a': 1, 'b': 2, 'c': 3}
print_params(**dict_)

print('----6----')

def print_params(a, b, c):
    print(a, b, c)

list_ = [1, 2]
dict_ = {'c': 3}
print_params(*list_, **dict_)

print('----7----')