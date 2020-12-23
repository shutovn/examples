'''
В трехзначном числе x зачеркнули его вторую цифру. Когда к образованному при этом
двузначному числу слева припи­сали вторую цифру числа x, то получилось число 546.
Найти число x.
'''

y = 546

a = int( y / 100 )
b = int( (y % 100) / 10 )
c = int( (y % 100) % 10 )

x =  b * 100 + a * 10 + c

print ("Число x = "+str(x))