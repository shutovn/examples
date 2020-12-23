'''
Дано трехзначное число, в котором все цифры различны.
Получить шесть чисел, образованных при перестановке цифр заданного числа.
'''

n = str(input("Введите трехзначное число: "))

numbers = []
for i in n[::]:
    numbers.append(i)

n1 = numbers[0]
n2 = numbers[1]
n3 = numbers[2]

print(n1+n2+n3)
print(n1+n3+n2)
print(n2+n3+n1)
print(n2+n1+n3)
print(n3+n2+n1)
print(n3+n1+n2)
