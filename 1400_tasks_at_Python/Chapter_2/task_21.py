# Составить программу расчета значения функций при любых значениях e, f, g и h.

import math

e = float(input("Введите значение e: "))
f = float(input("Введите значение f: "))
g = float(input("Введите значение g: "))
h = float(input("Введите значение h: "))

a = ( e + f / 2) / 3

b = math.fabs( h**2 - g )

c = math.sqrt((g - h)**2 - 3 * math.sin(e))

print ("При данных значениях a равен " + str(a))
print ("При данных значениях b равен " + str(b))
print ("При данных значениях c равен " + str(c))
