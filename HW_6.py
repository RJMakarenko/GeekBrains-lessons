# -*- coding: utf-8 -*-
# import time
#
#
# class TrafficLight:
#     def __init__(self):
#         self.__color = ['Red', 'Yellow', 'Green']
#
#     def running(self):
#
#         for ind, el in enumerate(self.__color):
#             t = 7 if ind == 0 or ind == 2 else 2
#             print(el)
#             time.sleep(t)
#
#
# tl_1 = TrafficLight()
# tl_1.running()

# Задание 2

# class Road:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def how_many(self, weight, layer_thickness):
#         print(f'{self._width} м * {self._length} м * {weight} кг * {layer_thickness} см = '
#               f'{((self._width * self._length * weight * layer_thickness) / 1000):.2f} т')
#
#
# r1 = Road(5000, 20)
# r1.how_many(25, 5)

# Задание 3

# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
#
# class Position(Worker):
#     def __init__(self, name, surname, position, wage, bonus):
#         super().__init__(name, surname, position, wage, bonus)
#
#     def get_full_name(self):
#         print(f'{self.name} {self.surname}')
#
#     def get_total_income(self):
#         total = 0
#         for res in self._income.values():
#             total += res
#         print(f'Общий доход: {total}')
#
#
# first = Position('Сергей', 'Петров', 'Менеджер', 10000, 2000)
# print(first.__dict__) # Выведем все доступные атрибуты объекта
# first.get_full_name() # Вызываем метод получения имени
# first.get_total_income() # Подсчитаем доход
# second = Position('Петр', 'Сергеев', 'Насяльника', 20000, 5000)
# print(second.position) # Обратимся к атрибуту Должность
# second.get_full_name()
# second.get_total_income()

# Задание 4

# class Car:
#     def __init__(self):
#         self.speed = 0
#         self.color = 'Black'
#         self.name = None
#         self.is_police = True if self.__class__ == PoliceCar else False
#
#     def go(self):
#         print('Поехали')
#         self.speed = 20
#         print(f'Текущая скорость {self.speed} км/ч')
#
#     def stop(self):
#         print('Остановка')
#         self.speed = 0
#
#     def turn(self, direction):
#         print(f'Поворачиваем {direction}')
#
#     def show_speed(self):
#         print(f'Текущая скорость {self.speed} км/ч')
#
#
# class TownCar(Car):
#     def show_speed(self):
#         print(self.speed)
#         if self.speed > 60:
#             print('Движение со скоростью выше 60 км/ч опасно!!!')
#
#
# class WorkCar(Car):
#     def show_speed(self):
#         print(self.speed)
#         if self.speed > 40:
#             print('Движение со скоростью выше 40 км/ч запрещено!!!')
#
#
# class SportCar(Car):
#     pass
#
#
# class PoliceCar(Car):
#     pass
#
#
# t_car = TownCar()
# t_car.color = 'White'
# t_car.go()
# t_car.stop()
# t_car.show_speed()
# t_car.speed = 70
# t_car.show_speed()
# print(t_car.is_police)
# p_car = PoliceCar()
# print(p_car.is_police)
# p_car.go()
# p_car.turn('направо')
# p_car.stop()
# s_car = SportCar()
# s_car.go()
# s_car.speed = 180
# s_car.show_speed()
# w_car = WorkCar()
# w_car.go()
# w_car.turn('налево')
# w_car.stop()
# w_car.show_speed()

# Задание 5

# class Stationery:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         print('Запуск отрисовки')
#
#
# class Pen(Stationery):
#     def __init__(self):
#         super(Pen, self).__init__('Ручка')
#
#     def draw(self):
#         print('Начинаем рисовать ручкой')
#
#
# class Pencil(Stationery):
#     def __init__(self):
#         super(Pencil, self).__init__('Карандаш')
#
#     def draw(self):
#         print('Рисуем карандашом')
#
#
# class Handle(Stationery):
#     def __init__(self):
#         super(Handle, self).__init__('Маркер')
#
#     def draw(self):
#         print('А теперь взяли в руки маркер')
#
#
# pen_1 = Pen()
# pen_1.draw()
# pencil_1 = Pencil()
# pencil_1.draw()
# handle_1 = Handle()
# handle_1.draw()
