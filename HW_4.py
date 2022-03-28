# Задание 1
# from sys import argv
#
# hours, rate_per_hour, prize = map(int, argv[1:])
# print(f'Ваша выработка в часах: {hours}')
# print(f'Ставка в час: {rate_per_hour}')
# print(f'Премия составила: {prize}')
# result = (hours * rate_per_hour) + prize
# print(f'Итоговая заработная плата: {result}')

# Задание 2
# sp = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# new_sp = [sp[i] for i in range(1, len(sp)) if sp[i] > sp[i - 1]]
# print(new_sp)

# Задание 3
# print(*[i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])

# Задание 4
# sp = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [x for x in sp if sp.count(x) == 1]
# print(result)

# Задание 5
# from functools import reduce
#
# result = reduce(lambda x, y: x * y, (x for x in range(100, 1001) if x % 2 == 0))
# print(result)

# Задание 6
# from itertools import count, cycle
# from sys import argv
# start = int(argv[1])
# print('Первые 20 чисел, начиная с указанного:')
# for i in count(start):
#     print(i, end=' ')
#     if i > start + 19:
#         break
# print()
# print('Повторяем элементы списка 4 раза:')
# sp = ['one', 'two', 'three', 'four']
# for i, j in enumerate(cycle(sp)):
#     print(j, end=' ')
#     if i >= (len(sp) * 4) - 1:
#         break

# Задание 7
# def fact(n):
#     start = 1
#     for i in range(1, n + 1):
#         start *= i
#         yield start
#
#
# for el in fact(8):
#     print(el)
