'''
Из трехзначного числа x вычли его последнюю цифру. Когда результат разделили на 10,
а к частному слева приписали последнюю цифру числа x, то получилось число 237. Найти число x.
'''

y = 237

# 2 это наша последняя цифра искомого числа, выделяем ее следующим образом в переменную
a = int( y / 100)

# узнаем остаток
b = 237 % 100

x = b * 10 + a

print ("Число x = "+str(x))