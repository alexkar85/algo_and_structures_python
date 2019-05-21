"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

# Цикл
list_1 = []
list_2 = []

number = input("Введите натуральное число: ")

for i in number:
    if int(i) % 2 == 0:
        list_1 += i
    else:
        list_2 += i

print(f"У натурального числа {number} чётных чисел {len(list_1)}: {list_1}, нечётных чисел {len(list_2)}: {list_2}")


# Рекурсия
list_1 = []
list_2 = []


number = int(input("Введите натуральное число: "))


def recursion(num):
    global list_1
    global list_2
    i = num % 10
    if i % 2 == 0:
        list_1 = [i] + list_1
    else:
        list_2 = [i] + list_2
    if num // 10 == 0:
        return
    recursion(num // 10)


recursion(number)

print(f"У натурального числа {number} чётных чисел {len(list_1)}: {list_1}, нечётных чисел {len(list_2)}: {list_2}")


# Рекурсия без массива
number = int(input("Введите натуральное число: "))


def even(num):
    i = num % 10
    if num // 10 == 0:
        if i % 2 == 0:
            return str(i)
        else:
            return ''
    else:
        if i % 2 == 0:
            return str(i) + even(num // 10)
        else:
            return '' + even(num // 10)


def noteven(num):
    i = num % 10
    if num // 10 == 0:
        if i % 2 == 0:
            return ''
        else:
            return str(i)
    else:
        if i % 2 == 0:
            return '' + noteven(num // 10)
        else:
            return str(i) + noteven(num // 10)


print(f"У натурального числа {number} чётные цифры {even(number)} , нечётные цифры {noteven(number)}")