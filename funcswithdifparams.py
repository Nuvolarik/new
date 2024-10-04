# def test_func(*params):
#     print('Тип:', type(params))
#     print('Аргумент:', params)
#
# test_func(1, 2, 3, 4)

print('----*----')

def summator(txt, *values):
    s = 0
    for i in values:
        s += i
    return f'{txt}{s}'

print(summator('Сумма чисел: ', 2, 3, 4))

print('----*----')

def summator(txt, *values, type = "sum"):
    s = 0
    for i in values:
        s += i
    return f'{txt}{s} {type}'

print(summator('Сумма чисел: ', 2, 3, 4, type = "summator"))

print('----*----')

def info(**values):
    print('Тип:', type(values))
    print('Аргумент:', values)

info(name = "Paul", course = "Python")

print('----*----')

def info(**values):
    print('Тип:', type(values))
    print('Аргумент:', values)
    for key, value in values.items():
        print(key, value)

info(name = "Paul", course = "Python")

print('----*----')

def my_sum(n, *args, txt="Сумма чисел"):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n
    print(txt + ":", s)

my_sum(1, 1, 2, 3, 4, 5)
my_sum(2, 2, 3, 4, 5, txt = "Сумма квадратов")