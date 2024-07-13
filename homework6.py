# Словари и множества

# Работа со словарем
my_dict = {'Anna': 1980, 'Vadim': 2008, 'Valeriya': 2002, 'Irina': 1956, 'Nikolay': 1955}
print('Словарь:', my_dict)
print('Существующее значение:', my_dict.get('Irina'))
print('Не существующее значение:', my_dict.get('Mikhail"'))
my_dict.update({'Artem': 2012, 'Katya': 2016})
del_item = my_dict.pop('Nikolay')
print('Удаленное значение:', del_item)
print('Скорректированный словарь:', my_dict)

# Работа с множеством
my_set = {15, 26, 'Apple', 45.15, 'Doll', 15, True, 26, 'Doll'}
print('Множество:', my_set)
my_set.add('Pear')
my_set.add(25.16)
my_set.discard('Apple')
print('Скорректированное множество:', my_set)
