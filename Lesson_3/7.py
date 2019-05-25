"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import randint


N = 10
a = [0] * N

for i in range(N):
    a[i] = randint(0, 10)

min_1 = a[0]
min_2 = a[1]
# ind_1 = 0
# ind_2 = 1

for i in range(2, N):
    if min_1 > min_2:
        min_1, min_2 = min_2, min_1
        # ind_1, ind_2 = ind_2, ind_1
    if min_2 > a[i]:
        min_2 = a[i]
        # ind_2 = i

print(f"Массив a: ", a)
print(f"Минимальный элемент 1: ", min_1)
# print(f"Индекс 1:", ind_1)
print(f"Минимальный элемент 2: ", min_2)
# print(f"Индекс 2:", ind_2)
