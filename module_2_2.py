first = 123
second = 456
third = 789

if third == second == first:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
print('_________')

first = 42
second = 69
third = 42

if third == second == first:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)