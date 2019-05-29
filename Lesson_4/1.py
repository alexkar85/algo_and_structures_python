"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

# Второй урок задание 7

import timeit
import cProfile


N = 10000000


def func1():
    a = 0
    f = True
    for n in range(1, N):
            if a + n != (n * (n + 1)) / 2:
                f = False
                break
            else:
                a = a + n

    if f:
        pass
        # return "Равенство выполняется"
    else:
        return "Равенство не выполняется"


print(timeit.timeit('func_1', number=100))
cProfile.run('func1()')


def func_2():
    a = 0
    for i in range(1, N):
        a += i
    if a == (N * (N + 1)) / 2:
        pass
        # return "Равенство выполняется"
    else:
        return "Равенство не выполняется"


print(timeit.timeit('func_1', number=100))
cProfile.run('func_2()')


#          4 function calls in 0.397 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.397    0.397 <string>:1(<module>)
#         1    0.397    0.397    0.397    0.397 Task_07.py:44(func1)
#         1    0.000    0.000    0.397    0.397 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# Равенство не выполняется
#          5 function calls in 0.079 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.079    0.079 <string>:1(<module>)
#         1    0.079    0.079    0.079    0.079 Task_07.py:62(func_2)
#         1    0.000    0.000    0.079    0.079 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#
# Process finished with exit code 0


# Рекурсия


K = 10


def func_3(i):
    if i == K:
        return i
    return i + func_3(i+1)


def run():
    sum = func_3(1)
    s = K*(K+1)/2
    if sum == s:
        print(f"Равенство выполняется")
    else:
        print(f"Равенство не выполняется")


cProfile.run('run()')


'''
func1 выполняется дольше оптимизрованной функции func2 почти в 5 раз из-за того, что на каждой итерации 
мы делаем проверку равенства функций 1+2+...+n = n(n+1)/2.
Если предположить что условия верно для всех n-1 значений, то нам остается доказать только для n-ого значения.
Такая оптимизация помогает нам сократить количество проверок и как следствие - время работы алгоритма.
В случае с рекурсией время выполнения большое из-за накладных расходов на дополнительные вызовы самой себя,
передачи аргумента и выделения памяти. Это приводит не только к медленно работе рекурсии, но и ограничениям 
количества рекурсивных вызовов.
'''