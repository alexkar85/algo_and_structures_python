"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""


###############################################################################
# Без использования коллекции

companies = []

n = k = int(input("Введите количество предприятий: "))

while k > 0:
    name = input("Введите наименование предприятия: ")
    q_1 = int(input("Введите прибыль за первый квартал: "))
    q_2 = int(input("Введите прибыль за второй квартал: "))
    q_3 = int(input("Введите прибыль за третий квартал: "))
    q_4 = int(input("Введите прибыль за четвёртый квартал: "))

    companies.append({'name': name, 'sum_': q_1 + q_2 + q_3 + q_4})

    k -= 1

sum = 0

for i in range(n):
    sum += companies[i]['sum_']

medium_year_sum = sum / n

list_1 = []
list_2 = []
list_3 = []

for i in range(n):
    if companies[i]['sum_'] > medium_year_sum:
        list_1.append(companies[i]['name'])
    elif companies[i]['sum_'] < medium_year_sum:
        list_2.append(companies[i]['name'])
    else:
        list_3.append(companies[i]['name'])

if len(list_1) > 0:
    print(f"Предприятие с прибылью выше среднего: {list_1}")
if len(list_2) > 0:
    print(f"Предприятие с прибылью ниже среднего: {list_2}")
if len(list_3) > 0:
    print(f"Предприятие с прибылью равной средней: {list_3}")


###############################################################################
# Используя коллекцию

import collections


companies = []
Company = collections.namedtuple('Company', ['name', 'sum_'])

n = k = int(input("Введите количество предприятий: "))

while k > 0:
    name = input("Введите наименование предприятия: ")
    q_1 = int(input("Введите прибыль за первый квартал: "))
    q_2 = int(input("Введите прибыль за второй квартал: "))
    q_3 = int(input("Введите прибыль за третий квартал: "))
    q_4 = int(input("Введите прибыль за четвёртый квартал: "))

    companies.append(Company(name=name, sum_=q_1 + q_2 + q_3 + q_4))

    k -= 1

sum = 0

for i in range(n):
    sum += companies[i].sum_

medium_year_sum = sum / n

list_1 = []
list_2 = []
list_3 = []

for i in range(n):
    if companies[i].sum_ > medium_year_sum:
        list_1.append(companies[i].name)
    elif companies[i].sum_ < medium_year_sum:
        list_2.append(companies[i].name)
    else:
        list_3.append(companies[i].name)

if len(list_1) > 0:
    print(f"Предприятие с прибылью выше среднего: {list_1}")
if len(list_2) > 0:
    print(f"Предприятие с прибылью ниже среднего: {list_2}")
if len(list_3) > 0:
    print(f"Предприятие с прибылью равной средней: {list_3}")