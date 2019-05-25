#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from random import randint


N = 10
a = [0] * N
b = [0] * N
j = 0

for i in range(N):
    a[i] = randint(-5, 5)


for i in range(N):
    if a[i] < 0:
        b[j] = a[i]
        j += 1

max_el = b[0]

for i in range(j):
    if b[i] > max_el:
        max_el = b[i]

print(f"Массив a = ", a)
if max_el == 0:
    print(f"Отрицательных элементов нет")
else:
    for i in range(N):
        if a[i] == max_el:
            print(f"Максимальный отрицательный элемент: ", max_el)
            print(f"Индекс максимального элемента: ", i)
            break
