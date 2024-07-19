# Задача "Все не так уж просто
# Объявляем переменные
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

# Выполняем перебор списка
for i in range(0, len(numbers)):
    is_prime = True
    if numbers[i] < 2:
        continue
    elif numbers[i] == 2:
        primes.append(numbers[i])
        continue
    for j in range(2, numbers[i]):
        if numbers[i] % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

# Вывод данных
print(f'Исходный список:{numbers}')
print(f'Простые числа:{primes}')
print(f'Составные числа:{not_primes}')
