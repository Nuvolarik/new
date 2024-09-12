print('хай, я строка в нижнем регистре'.replace('хай', 'пока'))

name = input("Введите Ваше имя: ")
current_year = 2024
date_of_birth = int(input("В каком году Вы родились? "))
age = current_year - date_of_birth
print("Здравствуйте,", name)
print("В этом году Вам", age, "лет")