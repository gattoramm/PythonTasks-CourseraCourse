# Дано целое число N. Выведите следующее за ним четное число.
# =========================
# Формат ввода
#
# Вводится целое положительное число, не превышающее 1000.
# =========================
# Формат вывода
#
# Выведите ответ на задачу.
# =========================
# Примеры
#
# Тест 1
# Входные данные:
# 7
#
# Вывод программы:
# 8
#
#
#
# Тест 2
# Входные данные:
# 8
#
# Вывод программы:
# 10

N = int(input())
print(N - N % 2 + 2)
