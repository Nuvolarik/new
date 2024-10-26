class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')

    def birthday(self):
        self.age += 1
        print(f'У меня день рождения, мне теперь {self.age}')

den = Human('Денис', 23)
max = Human('Макс', 45)

den.say_info()
max.say_info()
max.birthday()