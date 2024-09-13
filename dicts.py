phone_book = {'Paul': 89998885533, 'Kos': 87776661144}
print(phone_book['Paul'])

phone_book['Paul'] = 86668887755
print(phone_book)

del phone_book['Kos']
print(phone_book)

phone_book.update({'Olga': 24549681654,
                   'Bree': 68731346431})
print(phone_book)

print(phone_book.get('Raisa', 'Такого контакта нет'))
phone_book.pop('Bree')
print(phone_book)

print(phone_book.keys())
print(phone_book.values())
print(phone_book.items())

set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4}
print(set_)

set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'String', True, (1, 2, 3)}
list_ = [1, 1, 1, 1, 1, 2, 3, 2, 2]
list_ = set(list_)
print(list_)

set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'String', True, (1, 2, 3)}
list_ = [1, 1, 1, 1, 1, 2, 3, 2, 2]
list_ = set(list_)
print(list_.remove(1))
print(list_)
print(list_.add(4))
print(list_)
