# Составить программу расчета значения функций

import math

a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))

x = ( 2 / (a**2 + 25) + b ) / ( math.sqrt(b) + (a + b) / 2 )
y = ( math.fabs(a) + 2 * math.sin(b) ) / ( 5.5 * a )

print ("При данных значениях x равен " + str(x))
print ("При данных значениях y равен " + str(y))
