# Даны два целых числа. Найти:
# а) их среднее арифметическое;
# б) их среднее геометрическое.
import math

a = int(input("Введите a: "))
b = int(input("Введите b: "))

# среднее арифметическое
m = ( a + b )/2

# среднее геометрическое
x = math.sqrt( a * b )

print ("Ответы:")
print ("a) Среднее арифметическое чисел " + str(a) + " и " + str(b) + " равно: " + str(m) )
print ("б) Среднее геометрическое чисел " + str(a) + " и " + str(b) + " равно: " + str(x) )