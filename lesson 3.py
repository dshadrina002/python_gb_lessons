# 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.
# import random
# n = int(input('Enter quantity of elements in list: '))
# min = int(input('Enter min value: '))
# max = int(input('Enter max value: '))
# list = [random.randint(min, max) for i in range(n)]
# print(list)
# new_list = []
# for i in list:
#     if i not in new_list:
#          new_list.append(i)
# print(len(new_list))

# 19. Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# 23. Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)

# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
import random
n = int(input('Enter quantity of elements in list: '))
min = int(input('Enter min value: '))
max = int(input('Enter max value: '))
list = [random.randint(min, max) for i in range(n)]
print('Your list:')
print(list)
x = int(input('Enter amount you want find X: '))
count = 0
for i in list:
    if i == x:
        count +=1
print('How many times X meets in your list:')
print(count)

# Задача 18: Требуется найти в списке A самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
import random
n = int(input('Enter quantity of elements in list: '))
min = int(input('Enter min value: '))
max = int(input('Enter max value: '))
list = [random.randint(min, max) for i in range(n)]
print('Your list:')
print(list)
x = int(input('Enter amount you want find X: '))
close_to_x = 0
for i in list:
    if abs(x - i) < abs(x - close_to_x):
        close_to_x = i
print('Number close to X:')
print(close_to_x)