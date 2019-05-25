# 4.	Определить, какое число в массиве встречается чаще всего.

from random import randint


N = 10
a = [0] * N
dic = {}

for i in range(N):
    a[i] = randint(0, 5)
print(a)

for el in a:
    dic[el] = 0
# print(dic)

for el in a:
    dic[el] += 1
# print(dic)

max_el = 0
for value in dic.values():
    if value > max_el:
        max_el = value

for key, value in dic.items():
    if dic[key] == max_el:
        print(f"Число {key}, количество вхождений: {max_el}")
