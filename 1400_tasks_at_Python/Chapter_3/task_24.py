'''
Дано трехзначное число.
Найти число, полученное при перестановке первой и второй цифр заданного числа.
'''

n = str(input("Введите трехзначное число: "))

numbers = []
for i in n[::]:
    numbers.append(i)

print (numbers[1]+numbers[0]+numbers[2])