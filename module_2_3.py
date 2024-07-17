# Задача "Нули ничто, отрицание недопустимо!"

# Исходные данные
my_list = [42, 69, 0, 322, -13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
my_list_length = len(my_list)

# Формируем цикл
print(f'В заданом списке {my_list_length} чисел.')
print('В заданом списке следующие положительные числа:')
while i <= my_list_length - 1:
    if my_list[i] >= 0:
        print(my_list[i])
        if i == my_list_length - 1:
            print('Выведены все числа списка.')
            break
        i = i+1
        continue
    else:
        print('Следующее число списка отрицательное.')
        print(f'Выведено {i} чисел списка.')
        break
