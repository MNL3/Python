# Задача 26

# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def f(a, b):
#     if (b == 1):
#         return (a)
#     if (b != 1):
#         return (a * f(a, b - 1))
# a = int(input("Введите число: "))
# b = int(input("Введите значене степени: "))
# print("Результат = ", f(a, b))


# Задача 28
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

# def sum(a, b):
#     return a if b == 0 else sum(a + 1, b - 1) if a > 0 else sum(a - 1, b + 1)
    
# a, b = map(int, input().split())
# print("Сумма =", sum(a, b))