#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import randint


N = 10
a = [0] * N

for i in range(10):
    a[i] = randint(0, 100)

min_el = max_el = a[0]
min_index = max_index = 0

for i in range(10):
    if a[i] < min_el:
        min_el = a[i]
        min_index = i
    if a[i] > max_el:
        max_el = a[i]
        max_index = i

print(f"Массив a: ", a)
print(f"Минимальный элемент: ", min_el)
print(f"Индекс минимального элемента: ", min_index)

print(f"Максимальный элемент: ", max_el)
print(f"Индекс максимального элемента: ", max_index)

a[min_index], a[max_index] = max_el, min_el
min_index, max_index = max_index, min_index


print(f"Массив a: ", a)
print(f"Минимальный элемент: ", min_el)
print(f"Индекс минимального элемента: ", min_index)

print(f"Максимальный элемент: ", max_el)
print(f"Индекс максимального элемента: ", max_index)
