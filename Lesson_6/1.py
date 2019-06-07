"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

from pympler import asizeof

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

    sizesum = asizeof.asizeof(N) + asizeof.asizeof(a) + asizeof.asizeof(f) + asizeof.asizeof(n) 
    sizesum += asizeof.asizeof(range(1, N)) + asizeof.asizeof("Равенство выполняется") 
    sizesum += asizeof.asizeof("Равенство не выполняется")
    print(f"Алгоритм занимает {sizesum} байт")

    if f:
        return "Равенство выполняется"
    else:
        return "Равенство не выполняется"


K = 10
recsizesum = 0

def func3(i):
    global recsizesum
    recsizesum += asizeof.asizeof(i)
    if i == K:
        return i
    return i + func3(i+1)

def func3start():
    sum = func3(1)
    s = K*(K+1)/2

    sizesum = asizeof.asizeof(K) + asizeof.asizeof(sum) + asizeof.asizeof(s) + recsizesum
    sizesum += asizeof.asizeof("Равенство выполняется") + asizeof.asizeof("Равенство не выполняется")
    print(f"Алгоритм занимает {sizesum} байт")

    if sum == s:
        return "Равенство выполняется"
    else:
        return "Равенство не выполняется"

func1()
func3start()

# Рабочее окружение:
#   Python version 3.7.0
#   Windows 64-bit
# Анализ:
#   Рекурсивный алгоритм более требователен к памяти, потому что
#   при каждом вызове функции (рекурсивном вызове) все локальные
#   переменные внутри этой функции создаются на стеке заново.
#   Тот же самый алгоритм, но написанный через цикл не требует
#   столько памяти, сколько требует рекурсия.
#   По этой причине мы можем вызывать рекурсию только ограниченное
#   количество раз.
