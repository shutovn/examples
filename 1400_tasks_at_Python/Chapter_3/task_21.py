'''
Дано трехзначное число.
Найти число, полученное при прочтении его цифр справа налево.
'''
n = str(input("Введите трехзначное число: "))

numbers = []
for i in n[::-1]:
    numbers.append(i)

print (numbers[0]+numbers[1]+numbers[2])
