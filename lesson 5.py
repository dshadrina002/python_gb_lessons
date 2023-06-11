# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# import random
# n = int(input('Enter quantity of elements in list: '))
# min = int(input('Enter min value: '))
# max = int(input('Enter max value: '))
# list = [random.randint(min, max) for i in range(n)]
# print("Your list:", list)
# for i in range(n):
#     if list[i] == max:
#         list[i] = min
# print(list)

# Задача №35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

# def check(n):
#     counter = 0
#     for i in range (1, n+1):
#         if n % i ==0:
#             counter +=1
#     if counter == 2:
#         return print('Prime')
#     else:
#         return print('NOT Prime')
# number = int(input('Enter number: '))
# check(number)

# Задача №37. Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
import random
n = int(input('Enter quantity of elements in list: '))
list = [random.randint(0, 1000) for i in range(n)]
print("Your list:", list)
print("Reverse list:", list[::-1])