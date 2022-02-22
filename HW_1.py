# Задание 1
# some_variable = input('Введите что нибудь: ')
# print(f'Вы ввели: {some_variable}')
# some_number = int(input('А теперь введите любое число: '))
# print(f'Вы ввели число {some_number}, а квадрат этого числа равен {some_number ** 2}')

# Задание 2 вариант 1
# seconds = int(input('Введите количество секунд: '))
# hours = seconds // 3600
# minutes = seconds // 60 - hours * 60
# new_seconds = seconds - hours * 3600 - minutes * 60
# print(f'{seconds} секунд - это {hours:02d}:{minutes:02d}:{new_seconds:02d}')

# Задание 2 вариант 2
# seconds = int(input('Введите количество секунд: '))
# hours = seconds // 3600
# new_seconds = seconds % 3600
# minutes = new_seconds // 60
# new_seconds %= 60
# new_seconds = seconds - hours * 3600 - minutes * 60
# print(f'{seconds} секунд - это {hours:02d}:{minutes:02d}:{new_seconds:02d}')

# Задание 3
# n = input('Введите число n: ')
# print(f'{int(n) + int(n*2) + int(n*3)}')

# Задание 4
# n = int(input('Введите целое положительное число: '))
# mx = -1
# while n > 0:
#     mx = max(mx, n % 10)
#     n //= 10
# print(f'Максимальная цифра - {mx}')

# Задание 5
# plus = int(input('Введите сумму выручки: '))
# minus = int(input('Введите сумму издержек: '))
# result = f'Прибыль в размере {plus - minus}' if plus > minus else f'Убыток в размере {minus - plus}'
# print(result)

# Задание 6
# plus = int(input('Введите сумму выручки: '))
# minus = int(input('Введите сумму издержек: '))
# if plus > minus:
#     result = f'Прибыль в размере {(plus / minus) * 100} %'
#     staff_count = int(input('Введите количество сотрудников: '))
#     result += f'\n Прибыль на одного сотрудника - {(plus - minus) // staff_count}'
# else:
#     result = f'Убыток в размере {minus - plus}'
# print(result)

# Задание 7
# a = int(input('Введите результат за первый день: '))
# b = int(input('Введите желаемый результат: '))
# days_count = 1
# print('Результат:')
# print(f'{days_count}-й день: {a:.2f}')
# while a <= b:
#     days_count += 1
#     a += (a / 100) * 10
#     print(f'{days_count}-й день: {a:.2f}')
#
# print(f'Ответ: на {days_count} день спортсмен достиг результата - не менее {b} км.')
