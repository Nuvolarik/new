for i in 1, 2, 3, 4:
    print(i)
print('----------')

for i in 'hello':
    print(i)
print('----------')

list_ = ['one', 'two', 'three']
for i in list_:
    if i == 'three':
        list_.remove((i))
print(list_)
print('----------')

list_ = ['one', 'two', 'three']

for i in range(5):
    print(i)
print(list_)
print('----------')

list_ = ['one', 'two', 'three']

for i in range(len(list_)):
    list_[i] = ' :('
print(list_)
print('----------')

list_ = ['one', 'two', 'three']
list_2 = [2, 3, 4, 5, 1]
sum_ = 0
for i in range(len(list_2)):
    sum_ += list_2[i]
print(sum_)
print('----------')

for i in range(1, 11, 2):
    print(i)
print('----------')

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} x {j} = {i*j}')
print('----------')

dict_ = {'a':1, 'b':2, 'c':3}
for i in dict_:
    print(i, dict_[i])
print('----------')

# or

dict_ = {'a':1, 'b':2, 'c':3}
for i, k in dict_.items():
    print(i, k)
print('----------')