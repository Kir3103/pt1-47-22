"""
Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще)
"""

x_1 = int(input('Введите число:'))
x_2 = x_1
W = 0
while x_1 > 0:
    digit = x_1 % 10
    W = W * 10 + digit
    x_1 = int(x_1 / 10)
if W == x_2:
    print('Число является палиндромом')
else:
    print('Число не является палиндромом')
