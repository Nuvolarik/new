tuple_ = 1, 2, 3, 4
tuple_2 = (1, 2, 3, 4)
tuple_3 = tuple([1, 2, 3, 4])
print(tuple_)
print(tuple_2)
print(tuple_3)

tuple_4 = ([1, 2], 0) + (1, 2)
print(tuple_4)
tuple_4[0][0] = 2
print(tuple_4)
tuple_4 = (3, 4) * 3
print(tuple_4)