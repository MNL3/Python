# Задача 30
# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# a1 = int(input("Первый элемент = "))
# d = int(input("Разность = "))
# n = int(input("Количество элементов = "))
# res = [a1 + (i - 1)* d for i in range (1, n + 1)]
# print(*res)

# Задача 32
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# индексы: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 7 10
# Вывод: [1, 9, 13, 14, 19]


# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# max = int(input("Заданный максимум = "))
# min = int(input("Заданный минимум = "))
# for i in range(0, len(list_1)):
#     if min <= list_1[i] <= max:
#       print(i, end=' ')

