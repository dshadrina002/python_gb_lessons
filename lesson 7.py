# Задача 49. Про орбиты
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
def S(x):
    if x[0] == x[1]:
        return 0
    return x[0] * x[1]

mult = list(map(S, orbits))
print(mult)
max = mult.index(max(mult))
print(orbits[max])

# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic -
# это функция, которая принимает объект и вычисляет его характеристику.

def filt(funk, arr):
    res = list(map(funk, arr))
    for i in range(len(res)-1):
        if res[i] != res[i+1]:
            return False
    return True


values = [0, 2, 10, 5, 14]
list1 = filt(lambda x: x % 2, values)
print(list1)

