# Условная конструкция. Операторы if, elif, else.

# Организуем ввод чисел для проверки
first = int(input('Ввведите первое целое число:'))
second = int(input('Ввведите второе целое число:'))
third = int(input('Ввведите третье целое число:'))

# Выполняем проверку равенства чисел
if first == second == third:
    print('Вы ввели 3 одинаковых числа')
elif first == second != third or first == third != second or first != second == third:
    print('Вы ввели 2 одинаковых числа')
else:
    print('Все введенные числа разные')
