'''
Дано натуральное число n (n > 999). Найти:
а) число сотен в нем;
б) число тысяч в нем.
'''

n = str(input("Введите число > 999: "))

numbers = []
for i in n[::-1]:
    numbers.append(i)

print("а) число сотен: "+str(numbers[2]))
print("б) число тысяч: "+str(numbers[3]))
