'''
Дано трехзначное число. Найти:
а) число единиц в нем;
б) число десятков в нем;
в) сумму его цифр;
г) произведение его цифр.
'''

n = str(input("Введите трехзначное число: "))

numbers = []
for i in n[::-1]:
    numbers.append(i)

sum = int(numbers[0])+int(numbers[1])+int(numbers[2])
comp = int(numbers[0])*int(numbers[1])*int(numbers[2])

print("a) число единиц = "+str(numbers[0]))
print("б) число десятков = "+str(numbers[1]))
print("в) сумма цифр = "+str(sum))
print("a) произведение цифр = "+str(comp))
