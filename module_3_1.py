# Счетчик вызовов

calls = 0


def count_calls():      # Счетчик вызовов
    global calls
    calls = calls + 1


def string_info(string):        # Функциф подсчета длины строки и преобразования ее в верхний и нижний регистр
    str_info = (len(string), string.upper(), string.lower())
    count_calls()
    return str_info


def is_contains(string, list_to_search):        # Проверяет наличие строки в перечне
    if string.lower() in [i.lower() for i in list_to_search]:
        count_calls()
        return True
    else:
        count_calls()
        return False


print(string_info('Hydraulic'))
print(string_info('Dinosaur'))
print(string_info('LaSt CaLL'))
print(is_contains('flag', ['FlAg', 'baNNer', 'Pennant']))
print(is_contains('House', ['village', 'citY', 'town']))
print(is_contains('key', ['ansWEr', 'HINt', 'KeY', 'ReplY']))
print(calls)
