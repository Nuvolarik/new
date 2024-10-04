while 1 > 0: # или команда True вместо конструкции 1 > 0
    number = int(input('Введите число: '))
    if number % 2 == 0:
        print('Число четное')
        continue
    else:
        print('Число нечетное')
print('Меня не забыли')
