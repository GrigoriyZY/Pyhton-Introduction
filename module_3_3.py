# "Распаковка позиционных параметров"


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# Задание 1
print('Задание 1:')
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*[15, 25, 'Test'])
print_params(5, 'Testing params', False)
print_params(b='Testing params')

# Задание 2
value_list = [15, 'Test', False]
value_dict = {'a': 1, 'b': 'test2', 'c': False}
print('Задание 2:')
print_params(*value_list)
print_params(**value_dict)

# Задание 3
value_list_2 = [54.32, 'Строка']
print('Задание 3')
print_params(*value_list_2)
print_params(*value_list_2, 42)
