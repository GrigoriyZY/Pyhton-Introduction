# Слишком древний шифр

def password(n): # Функциф для генерации проверки. В качестве аргумента принимает введенное число, воззвращает пароль.
    pass_ = []
    i = 1
    while i < n / 2:
        for j in range(i + 1, n + 1):
            if n % (i+j) == 0:
                pass_.append(i)
                pass_.append(j)
                continue
        i = i + 1
    return pass_


repeat = True
while repeat:
    n = int(input('Введите число из первой вставки:'))
    if n < 3 or n > 20:
        print('Вы ввели неверное число. Число должно быть в диапазоне от 3 до 20.')
        continue
    result = password(n)
    print(f'Пароль для введенного числа {n} следующий:{result}')
    reply = str(input('Хотите повторить7 (Да / Нет) '))
    if reply == 'Да':
        continue
    else:
        break
