"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""


import random


M = []

for i in range(0, 10):
        M.append(random.uniform(0, 49))

print(f"Исходный массив: {M}")


def func(A):
    n = len(A) // 2
    if n == 0:
        return A

    x = func(A[:n])
    y = func(A[n:])
    i = 0
    j = 0
    C = []
    
    while True: 
        if x[i] < y[j]:
            C.append(x[i])
            i += 1
            if i == len(x):
                for k in range(j, len(y)):
                    C.append(y[k])
                break
        else:
            C.append(y[j])
            j += 1
            if j == len(y):
                for k in range(i, len(x)):
                    C.append(x[k])
                break
    return C 

print(f"Отсортированный:", func(M))