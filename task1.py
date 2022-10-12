# 1. Используя библиотеки math, cmath и time сравните скорость вычисления квадратного корня,
# синуса и логарифма 1000000 раз из введённого пользователем числа. Алгоритм должен содержать
# проверку корректности входных данных. Результаты приведите в простой таблице.

# добавила стандартные библиотеки
import math
import cmath
import time

# пользователь вводит число
x = float(input())
# число итераций
count = 1000000


def print_time(f, count, x):
    time1 = time.time()
    list(map(lambda y: f(x), range(count)))
    time2 = time.time()
    return time2 - time1


funcs = (
    'math.sqrt',
    'math.log',
    'cmath.sqrt',
    'cmath.log',
)

for f in funcs:
    print(f, print_time(eval(f), count, x))
