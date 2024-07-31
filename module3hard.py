# Задание "Раз, два, три, четыре, пять .... Это не всё?":

def sum_list(test):                                 # Функция вычисляет сумму цифр
    s = 0
    if len(test) == 0:                              # Отсекаем пустые списки
        return s
    for i in range(len(test)):                      # Проверяем тип элемента и считаем сумму
        if isinstance(test[i], int):
            s = s + test[i]
        elif isinstance(test[i], str):
            s = s + len(test[i])
        elif isinstance(test[i], dict):             # Преобразуем словарь в список
            converted_dict = [*test[i].items()]
            s = s + sum_list(converted_dict)
        elif isinstance(test[i], (list, tuple)):
            s = s + sum_list(test[i])
        elif isinstance(test[i], set):              # Преобразуем множество в список
            converted_set = list(test[i])
            s = s + sum_list(converted_set)
    return s


# Исходный набор данных
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(f'Исходные данные:{data_structure}')
print(f'Сумма элементов:', sum_list(data_structure))
