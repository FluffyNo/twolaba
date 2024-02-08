# №1
# a = int(input('Введите целое число(-а) '))
#
# if a >= 1000:
#     print('Это число четырёхзначное')
# elif a >= 100 and a << 1000:
#     print('Это число трёхзначное')
# elif a >= 10 and a << 100:
#     print('Это число двухзначное')
# else:
#     print('Это число однозначное')

# №2
# arg1 = float(input("Первое число: "))
# arg2 = float(input("Второе число: "))
# arg3 = float(input("Третье число: "))
#
# if arg1 and arg2 > arg3:
#     print(f'Наибольшие числа {arg1, arg2}')
# elif arg2 and arg3 > arg1:
#     print(f'Наибольшие числа {arg2, arg3}')
# elif arg3 and arg1 > arg2:
#     print(f'Наибольшие числа {arg3, arg1}')

# №3
# A = float(input("Введите значение переменной A: "))
# B = float(input("Введите значение переменной B: "))
# C = float(input("Введите значение переменной C: "))
#
# if (A < B < C) or (A > B > C):
#     A *= 2
#     B *= 2
#     C *= 2
# else:
#     A = -A
#     B = -B
#     C = -C
#
# print("Новые значения переменных A, B, C:")
# print("A =", A)
# print("B =", B)
# print("C =", C)

# №4
# import math
#
# def f(x):
#     if x > 0:
#         return 2 * math.sin(x)
#     else:
#         return 6 - x
#
# x = float(input("Введите значение x: "))
#
# result = f(x)
# print("Значение функции f(x) при x =", x, "равно", result)

# №5
# def descnum(num):
#     if num == 0:
#         return "нулевое число"
#     elif num > 0:
#         if num % 2 == 0:
#             return "положительное четное число"
#         else:
#             return "положительное нечетное число"
#     else:
#         if num % 2 == 0:
#             return "отрицательное четное число"
#         else:
#             return "отрицательное нечетное число"
#
# number = float(input("Введите целое число: "))
# description = descnum(number)
# print("Описание числа:", description)