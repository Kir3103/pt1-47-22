"""
Дана строка. Удалите из нее все символы, чьи индексы делятся на 3
"""

str_ = input('Введите строку:')
str_ = str_.replace(' ', '')
new_str = ''
for i in range(len(str_)):
    if i % 3 != 0:
        new_str = new_str + str_[i]
print('Новая строка:', new_str)


"""
Длина Московской кольцевой автомобильной дороги —109 километров.
Байкер Вася стартует с нулевого километра МКАД и едет со скоростью v километров в час.
На какой отметке он остановится через t часов?
Программа получает на вход значение v и t. Если v>0, то Вася движется в положительном направлении
по МКАД, если же значение v<0, то в отрицательном.
Программа должна вывести целое число от 0 до 108 — номер отметки, на которой остановится Вася.
"""

v = float(input('Скорость движения:'))
t = float(input('Время в пути:'))
dist = 109
mark_km = 0
if v > 0:
    mark_km = int((v * t) % dist)
    print('Байкер находится на отметке:', mark_km)
else:
    mark = int(abs(dist - (abs(v * t)) % dist))
    print('Байкер находится на отметке:', mark_km)


"""
С начала суток прошло H часов, M минут, S секунд (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).
По данным числам H, M, S определите угол (в градусах), на который повернулаcь часовая стрелка с
начала суток и выведите его в виде действительного числа.
"""

H = int(input('Часы:'))
M = int(input('Минуты:'))
S = int(input('Секунды:'))
Deg = H * 30 + M * 30 / 60 + S * 30 / 3600
print('Угол равен', Deg, 'градусов')
