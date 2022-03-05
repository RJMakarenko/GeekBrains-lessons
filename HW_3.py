# Задание 1

# def division(x, y):
#     try:
#         result = x / y
#         return result
#     except ZeroDivisionError:
#         return 'Деление на 0'

# Задание 2
#
# def user_info(name='', surname='', year=1800, city='', email='', phone=''):
#     print(name, surname, year, city, email, phone, sep=' ')
#
#
# user_info(name='Василий', surname='Васильев', year=1980, city='Краснодар',
#           email='user@test.com', phone='+7-666-66-66-66')

# Задание 3

# def my_func(a, b, c):
#     """
#     Функция принимает на вход 3 параметра
#     a: Целое число
#     b: Целое число
#     c: Целое число
#     Возвращает сумму двух наибольших
#     """
#     lst = sorted([a, b, c])
#     return sum(lst[1:])
#
#
# print(my_func(10, 1, 12))
# Задание 4

# def my_func(x, y):
#     return x**y
#
# def my_func(x, y):
#     result = 1
#     for i in range(abs(y)):
#         result *= x
#     return 1 / result

# Задание 5

# def some_sum():
#     result = 0
#     while True:
#         numbers = input().split()
#         for el in numbers:
#             try:
#                 result += int(el)
#             except ValueError:
#                 print(result)
#                 return
#         print(result)
#
#
# some_sum()

# Задание 6
#
# def int_func(text):
#     return text.capitalize()

# Задание 7
# def int_func(text):
#     return text.capitalize()
#
#
# s = 'приветствую замечательного преподавателя поставьте 5 пожалуйста )))' #Здесь конечно нужно поменять на input()
# result = [x for x in map(lambda word: int_func(word), s.split())]
# print(*result)
