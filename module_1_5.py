immutable_var = "search", True, (1, 3, 8)
print(immutable_var)

#immutable_var[2] = 555
#print(immutable_var)
# Python не дает изменить отдельный элемент внутри кортежа

mutable_list = ["research", False, (8, 3, 1)]
print(mutable_list)
mutable_list.append("Modified")
print(mutable_list)