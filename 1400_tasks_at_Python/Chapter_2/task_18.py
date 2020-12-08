# Составить программу вычисления значений функций
import math

x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))

z = (x + ( 2 + y )/ x**2 ) / (y + 1 / math.sqrt(x**2 + 10))
q = 7.25 * math.sin(x) - math.fabs(y)

print ("При данных значениях z равен " + str(z))
print ("При данных значениях q равен " + str(q))
