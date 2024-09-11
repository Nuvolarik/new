
def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount <= balance:
        return balance - amount, True
    else:
        return balance, False

def main():

    balance = 0

    while True:
        print('1: Проверить баланс')
        print('2: Внести деньги')
        print('3: Снять деньги')
        print('4: Выход из программы')
        choice = input('Выберите действие: ')

        if choice == '1':
            print(f'Ваш текущий баланс равен {balance} руб.')
        elif choice == '2':
            amount = int(input('Введите сумму для внесения: '))
            if amount > 0:
                balance = deposit(balance, amount)
                print(f'Вы успешно внесли {amount} руб. Текущий баланс {balance} руб.')
            else:
                print('Сумма должна быть положительная.')
        elif choice == '3':
            amount = int(input('Введите сумму для снятия: '))
            if amount > 0:
                balance, success = withdraw(balance, amount)
                if success:
                    print(f'Вы успешно сняли {amount} руб. Ваш текущий баланс равен: {balance} руб.')
                else:
                    print('Недостаточно средств на балансе!')
            else:
                print('Сумма должна быть положительной!')
        elif choice == '2':
            print('Выход из программы')
            break
        else:
            print('Некорректный выбор. Попробуйте снова!')

main()