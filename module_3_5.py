# Реверсивное умножение цифр


def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0:1])
    if len(str_number[1:]) >= 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    elif len(str_number[1:]) < 1:
        return first


n = int(input('Введите произвольное число:'))
result = get_multiplied_digits(n)
print(result)
