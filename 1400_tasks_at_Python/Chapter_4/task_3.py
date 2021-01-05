'''
Рассчитать значение у при заданном значении х:
При x > 0 y = sinx^2
В противном случае y = 1 + 2*sin^2x  " sin^2x = (1 - cos2x)/2 "
'''
import math

x = float(input("Введите значение x: "))

if x > 0:
    y = math.sin(x**2)
    z = "больше ноля"
else:
    y = 1 + (1 - math.cos(2 * x))
    z = "меньше ноля"

print("Значение x - "+str(z),"и y = "+str(y))
