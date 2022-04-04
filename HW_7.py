# -*- coding: utf-8 -*-
# Задание 1

# class Matrix:
#     def __init__(self, lst):
#         self.matrix = lst
#
#     def __str__(self):
#         string = ''
#         for el in self.matrix:
#             for i in range(len(el)):
#                 string += str(el[i]) + '\t\t'
#             string += '\n'
#         return string
#
#     def __add__(self, other):
#         result = []
#         for i in range(len(self.matrix)):
#             res = []
#             for j in range(len(self.matrix)):
#                 res.append(self.matrix[i][j] + other.matrix[i][j])
#             result.append(res)
#         return Matrix(result)
#
#
# m1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
# print(m1)
# m2 = Matrix([[31, 32, 188], [-45, 21, 124], [-3, 54, 178]])
# print(m2)
# m3 = Matrix([[12, 23, 232, 23], [23, 55, 65, 45]])
# print(m3)
# print(m1 + m2)

# Задание 2

# class Clothes:
#     def __init__(self, size=0, height=0):
#         self.size = size
#         self.height = height
#
#
# class Coat(Clothes):
#     def __init__(self, size):
#         super().__init__(size=size)
#
#     @property
#     def material_consumption(self):
#         return 'Расход материала: ' + str((self.size / 6.5) + 0.5) + ' м.'
#
#
# class Suit(Clothes):
#     def __init__(self, height):
#         super().__init__(height=height)
#
#     @property
#     def material_consumption(self):
#         return 'Расход материала: ' + str((2 * self.height / 100) + 0.3) + ' м.'
#
#
# coat1 = Coat(52)
# print(coat1.__dict__)
# print(coat1.material_consumption)
# suit1 = Suit(185)
# print(suit1.__dict__)
# print(suit1.material_consumption)

# Задание 3

# class Cell:
#     def __init__(self, quantity):
#         self.quantity = quantity
#
#     def __add__(self, other):
#         return Cell(self.quantity + other.quantity)
#
#     def __sub__(self, other):
#         return Cell(self.quantity - other.quantity) if (self.quantity - other.quantity) > 0 else 'Результат ' \
#                                                                                                  'отрицательный '
#
#     def __mul__(self, other):
#         return Cell(self.quantity * other.quantity)
#
#     def __truediv__(self, other):
#         return Cell(self.quantity // other.quantity)
#
#     def __str__(self):
#         return '*' * self.quantity
#
#     def make_order(self, number):
#         res = ''
#         for i in range(self.quantity // number):
#             res += '*' * number + '\n'
#         res += '*' * (self.quantity % number)
#         return res
#
#
# c1 = Cell(7)
# c2 = Cell(2)
# c3 = c1 + c2
# print(c1 + c2)
# print(c1 * c2)
# print(c1 - c2)
# print(c2 - c1)
# print(c3)
# c4 = c1 + c2 + c3
# print(c4.make_order(4))
# print(c4 / c2)