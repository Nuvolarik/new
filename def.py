import random


def say_hello():
    print("Hello!")
print('-------')

say_hello()

def say_hello(name):
    print("Hello!", name)
print('-------')

say_hello('Paul')
say_hello('Kirill')
say_hello('Sofia')

def lottery():
    tickets = [1,2,3,4,5,6,7,8,9,10]
    win = random.choice(tickets)
    return win

win = lottery()
print(win)
print('-------')