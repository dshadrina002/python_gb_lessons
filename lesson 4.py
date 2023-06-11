# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D,
# G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.

# scrabble_dict = {'A': 1, 'E': 1, 'I': 1, 'K': 2 }
# some_str = input()
# summa = 0
#
# for letter in some_str:
#     summa += scrabble_dict[letter]
# print(summa)

# 25. Напишите программу, которая принимает на вход строку,
# и выводит на экран кол-во повторений каждого из символов
# some_dict = {}
# word = input()
# for letter in word:
#     if letter not in some_dict:
#         some_dict[letter] = 1
#     else:
#         some_dict[letter] +=1
# print(some_dict)

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# n = int(input('Enter quantity of elements in set 1: '))
# set1 = set()
# for i in range(n):
#     num1 = int(input('Enter value to set 1: '))
#     set1.add(num1)
#
# m = int(input('Enter quantity of elements in set 2: '))
# set2 = set()
# for i in range(m):
#     num2 = int(input('Enter value to set 2: '))
#     set2.add(num2)
#
# intersection = set1.intersection(set2)
# result = sorted(intersection)
# print("Числа, встречающиеся в обоих множествах без повторений:", result)

# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.

some_str = input()
some_list = some_str.split()
some_set = set ()
for word in some_list:
    if not word[-1].isalpha():
        word = word[:-1]
    some_set.add(word)
print(len(some_set))