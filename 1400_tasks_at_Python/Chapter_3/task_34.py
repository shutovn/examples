'''
В трехзначном числе x зачеркнули первую цифру. Когда
оставшееся число умножили на 10, а произведение сложили с первой цифрой числа x,
то получилось число 564. Найти число x.
'''

n = 564

# узнаем первую цифру
n1 = n % 10

# Делим на 10 и подставляем цифру вперед
x = str(n1)+str(int((n - n1) / 10))

print ("Число x = "+str(x))