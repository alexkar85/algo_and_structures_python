"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

numbers = input("Введите натуральные числа через пробел: ")
numbers = numbers.split()
print(numbers)

max_num = 0
sum_max = 0


def func_sum(num):
    if num // 10 == 0:
        return num
    else:
        return num % 10 + func_sum(num // 10)


for i in numbers:
    if func_sum(int(i)) > sum_max:
        max_num = i
        sum_max = func_sum(int(i))

print(f"Натуральное число: {max_num}, сумма его чисел: {sum_max}")