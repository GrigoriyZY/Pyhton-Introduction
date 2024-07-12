# Неизменяемые и изменяемые объекты. Кортежи и списки
# Кортеж
immutable_var = 25, 'food', True, [15, 22]
print(immutable_var)
immutable_var[3][0] = 22
print(immutable_var)

# Список
mutable_list = [125, False, 'drink', 15]
print(mutable_list)
mutable_list[1] = True
print(mutable_list)
mutable_list.append('дополнение')
mutable_list.extend([25, False])
mutable_list.remove(125)
print(mutable_list)
