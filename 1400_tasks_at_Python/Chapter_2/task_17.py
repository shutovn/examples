# Даны основания и высота равнобедренной трапеции. Найти ее периметр.

# a верхнее основание
# b нижнее основание
# h высота
import math

a = float(input ("Введите значение большего основания трапеции "))
b = float(input ("Введите значение меньшего основания трапеции "))
h = float(input ("Введите значение высоты трапеции "))

P = a + b + 2 * math.sqrt((h)**2 + ((a-b) / 2)**2)

print ("Периметр р/б трапеции равен " + str(P))