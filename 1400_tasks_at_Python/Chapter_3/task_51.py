'''
Задачи повышенной сложности

Даны два целых числа a и b. Если a делится на b или b
делится на a, то вывести 1, иначе – любое другое число.
Условные операторы и операторы цикла не использовать.
'''

a = int(input("Введите число а: "))
b = int(input("Введите число b: "))

x1 = a % b
x2 = b % a
x = x1 * x2 + 1

print("Если a делится на b или b делится на a, то вывести 1, иначе – любое другое число:", x)
