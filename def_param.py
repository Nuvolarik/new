from operator import truediv
from random import random


def say_hi(name):
    print('Hi!', name)

say_hi('Fil')
say_hi('Alex')
say_hi('Jack')

print('--------')

#import random
#def lottery():
#    tickets = [1,2,3,4,5,6,7,8,9]
#    win = random.choice(tickets)
#    return win

#win = lottery()
#print(win)

print('--------')

#import random
#def lottery(mon, sun):
#    tickets = [1,2,3,4,5,6,7,8,9,10]
#    win1 = random.choice(tickets)
#    tickets.remove(win1)
#    win2 = random.choice(tickets)
#    print(mon, sun)
#    return win1, win2

#win1, win2 = lottery(mon: 'mon', sun:'sun')
#print(win1, win2)
print('--------')

def test(a = 2, b = True):
    print(a, b)

test(*[1, 2])