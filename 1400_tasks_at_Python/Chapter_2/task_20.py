# Составить программу расчета значения функций при любых значениях e, f, g и h.

import math

e = float(input("Введите значение e: "))
f = float(input("Введите значение f: "))
g = float(input("Введите значение g: "))
h = float(input("Введите значение h: "))

a = math.sqrt( math.fabs(e - 3/f)**3 + g )

b = math.sin(e) + math.cos(h)**2

c = ( 33 * g ) / ( e * f - 3 )

print ("При данных значениях a равен " + str(a))
print ("При данных значениях b равен " + str(b))
print ("При данных значениях c равен " + str(c))
