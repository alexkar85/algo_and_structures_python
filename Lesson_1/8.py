# 8.	Определить, является ли год, который ввел пользовательт,
# високосным или не високосным.
#Год является високосным в двух случаях: либо он кратен 4,
# но при этом не кратен 100, либо кратен 400.

year = int(input("Введите год: "))

if (year % 400) == 0:
    print("Год: ", year, " - является високосным")
elif (year % 4) == 0 and (year % 100) != 0:
    print("Год: ", year, " - является високосным")
else:
    print("Год: ", year, " - является не високосным")
