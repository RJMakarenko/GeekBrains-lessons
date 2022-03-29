# Задание 1

# with open('test.txt', 'w') as txt_file:
#     s = input()
#     while s:
#         print(s, file=txt_file)
#         s = input()

# Задание 2

# with open('test.txt') as txt_file:
#     sp = txt_file.readlines()
#     print(f'Количество строк: {len(sp)}')
#     for ind, el in enumerate(sp):
#         words = el.split()
#         print(f'{ind+1}-я строка: {len(words)}')

# Задание 3

# zp = []
# with open('test.txt') as f:
#     sp = f.readlines()
#     for el in sp:
#         money = float(el.strip().split()[-1])
#         zp.append(money)
#         if money < 20000:
#             print(el.strip().split()[0])
# print(f'Средний оклад: {(sum(zp)/len(zp)):.2f}')

# Задание 4

# numerals = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
# Input = open('test.txt')
# Output = open('new.txt', 'w')
# input_data = Input.readlines()
# for el in input_data:
#     text = el.split()
#     new_text = numerals[text[0]] + ' '
#     new_text += ' '.join(text[1:])
#     print(new_text, file=Output)
# Input.close()
# Output.close()

# Задание 5
# from random import randint
#
# with open('file.txt', 'w') as f1, open('file.txt', 'r') as f2:
#     for i in range(2):
#         print(randint(1, 100), file=f1, end=' ')
#     f1.seek(0)
#     sp = map(int, f2.readline().split())
# print(sum(sp))

# Задание 6

# subjects = {}
# with open('file.txt') as f1:
#     while True:
#         hours = 0
#         string = f1.readline().split()
#         if not string:
#             break
#         for el in string[1:]:
#             hours += int(''.join(x for x in list(el) if x.isdigit()))
#         if string[0] not in subjects:
#             subjects[string[0]] = hours
#         else:
#             subjects[string[0]] += hours
# print(subjects)

# Задание 7

