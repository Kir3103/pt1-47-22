"""
Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится
"""

f1 = 0
f2 = 1
n = int(input('Введите число:'))
i = 0
while i < n - 2:
    f = f1 + f2
    f1 = f2
    f2 = f
    i = i + 1
print('Число Фибоначчи:', f2)
