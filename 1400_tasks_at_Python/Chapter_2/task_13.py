# Составить программу решения линейного уравнения ax + b = 0 (a ≠ 0).

print ("Для решения линейного уравнения ax + b = 0 (a ≠ 0), введите значения a и b ")

a = int(input("Введите значение а: "))
b = int(input("Введите значение b: "))

x = - b / a

print ("При условии, что (a ≠ 0), x = -b/a")
print ("Ответ: х = " + str(x) )