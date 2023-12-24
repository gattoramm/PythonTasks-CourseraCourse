# Длина Московской кольцевой автомобильной дороги — 109 километров. Байкер Вася стартует с нулевого километра МКАД
# и едет со скоростью v километров в час. На какой отметке он остановится через t часов?
# ============================
# Формат ввода
#
# Программа получает на вход значение v и t. Если v>0, то Вася движется в положительном направлении по МКАД, если
# же значение v<0, то в отрицательном. (Гарантируется, что исходные числа — целые и находятся в промежутке
# от -1000 до +1000).
# ============================
# Формат вывода
#
# Программа должна вывести целое число от 0 до 108 — номер отметки, на которой остановится Вася.
# ============================
# Примеры
#
# Тест 1
# Входные данные:
# 60
# 2
#
# Вывод программы:
# 11

v = int(input())
t = int(input())
print((v*t) % 109)
