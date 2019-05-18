import random

int_1 = int(input("Введите первое целое число: "))
int_2 = int(input("Введите второе целое число: "))
float_1 = int(input("Введите первое вещественное число: "))
float_2 = int(input("Введите второе вещественное число: "))
char_1 = input("Введите первый символ (a-z): ")
char_2 = input("Введите первый символ (a-z): ")

# Случайное целое число
if int_1 < int_2:
    int_3 = random.randint(int_1, int_2 + 1)
else:
    int_3 = random.randint(int_2, int_1 + 1)

# Случайное вещественное число
float_3 = random.uniform(float_1, float_2)

# Приведение символов к нижмему регистру
char_1 = char_1.lower()
char_2 = char_2.lower()

# Определение позиции символа в таблице юникода
chr_1 = ord(char_1)
chr_2 = ord(char_2)

# Случайный символ
if chr_1 < chr_2:
    chr_3 = random.randrange(chr_1, chr_2 + 1)
else:
    chr_3 = random.randrange(chr_2, chr_1 + 1)
char_3 = chr(chr_3)

print(f"Случайное целое число в диапазоне ({int_1},{int_2}): {int_3}")
print(f"Случайное вещественное число в диапазоне ({float_1},{float_2}): {float_3}")
print(f"Случайный символ в диапазоне ({char_1},{char_2}): {char_3}")
