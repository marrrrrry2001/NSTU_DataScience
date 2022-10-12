# 1. Используя библиотеки math, cmath и time сравните скорость вычисления квадратного корня,
# синуса и логарифма 1000000 раз из введённого пользователем числа. Алгоритм должен содержать
# проверку корректности входных данных. Результаты приведите в простой таблице.

# добавила стандартные библиотеки
import math
import cmath
import time

# пользователь вводит число
x = float(input())
# добавила вычисление корня и логарифма из библиотек math и cmath с помощью анонимной функции
math_sqrt, math_log = lambda x: math.sqrt(x), lambda x: math.log(x)
cmath_sqrt, cmath_log = lambda x: cmath.sqrt(x), lambda x: cmath.log(x)

# время начала и конца выполнения
time1 = time.time()
for __ in range(1000000):
    math_sqrt(x)
time2 = time.time()
for __ in range(1000000):
    math_log(x)
time3 = time.time()
for __ in range(1000000):
    cmath_sqrt(x)
time4 = time.time()
for __ in range(1000000):
    cmath_log(x)
time5 = time.time()

# вывод в консоль
print('time math_sqrt after 1000000 iterations: ', abs(time1 - time2))
print('time math_log after 1000000 iterations:  ', abs(time2 - time3))
print('time cmath_sqrt after 1000000 iterations:', abs(time3 - time4))
print('time cmath_log after 1000000 iterations: ', abs(time4 - time5))
