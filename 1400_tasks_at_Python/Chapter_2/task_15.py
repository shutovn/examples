# Найти площадь кольца по заданным внешнему и внут­реннему радиусам.
import math

R = float(input("Введите радиус R внешней окружности: "))
r = float(input("Введите радиус r внутренней окружности: "))
pi = round(math.pi, 3)

S = pi * ( R**2 - r**2 )

print ("Площадь кольца равна " + str(S))
