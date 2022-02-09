"""
Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще)
"""

x_1 = int(input('Введите число:'))
x_2 = x_1
result = 0
while x_1 > 0:
    digit = x_1 % 10
    result = result * 10 + digit
    x_1 = int(x_1 / 10)
if result == x_2:
    print('Число является палиндромом')
else:
    print('Число не является палиндромом')