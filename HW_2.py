# Задание 1

# some_list = [1, 2.5, 'Element', (1, 5), [2, 5, 6], {'Ivanov': 5}, {1, 5, 6, 8}]
# for ind, el in enumerate(some_list):
#     print(f'Элемент с индексом {ind} имеет тип: {type(el)}')

# Задание 2

# n = int(input('Введите количество элементов списка: '))
# some_list = []
# for i in range(n):
#     some_list.append(input())
# print(some_list)
# for i in range(0, len(some_list) - 1, 2):
#     some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]
# print(some_list)

# Задание 3

# n = int(input('Введите число от 1 до 12: '))
# seasons = [['Зима', 12, 1, 2], ['Весна', 3, 4, 5], ['Лето', 6, 7, 8], ['Осень', 9, 10, 11]]
# for el in seasons:
#     if n in el:
#         print(el[0])

# n = int(input('Введите число от 1 до 12: '))
# seasons = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5],  'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
# for season, number in seasons.items():
#     if n in number:
#         print(season)

# Задание 4
# s = input().split()
# for ind, word in enumerate(s, 1):
#     print(f'{ind} - {word[:10]}')

# Задание 5
# my_list = [7, 5, 3, 3, 2]
# new_num = int(input())
# if my_list[-1] <= new_num <= my_list[0]:
#     my_list.insert(my_list.index(new_num) + 1, new_num)
# elif new_num < my_list[-1]:
#     my_list.append(new_num)
# else:
#     my_list.insert(0, new_num)
# print(my_list)

# Задание 6
# Если правильно понял задание, то так

# some_list = [
#     (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
#     (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
#     (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
# ]
# new_dict = {}
# for el in some_list:
#     for key, value in el[1].items():
#         if key in new_dict:
#             new_dict[key] += [value]
#         else:
#             new_dict[key] = [value]
# print(new_dict)

