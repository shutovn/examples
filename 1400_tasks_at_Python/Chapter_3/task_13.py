'''
Замечание
В задачах 3.12–3.15 условный оператор не использовать.

Дана таблица из 10 строк и 5 столбцов. Определить:
1) в какой строке находится значение с порядковым номером
n, если нумерацию вести построчно сверху вниз, а в каждой строке – слева направо;
2) в какой строке находится это значение.

Примечание, от меня, на мой взгляд пункт 2 равнозначен пункту 1.
Предположу, что в пункте первом, помимо того, что необходимо найти строку, надо найти порядковый номер искомого числа в строке.
'''
import math
number = [5, 1, 2, 3, 4]
a = int(input("Введите число от 1 до 50: "))
n2 = math.ceil( a / 5 )

b = int(a / 5)
n1 = a - b * 5

print("1) Заданное число находится в "+str(n2)+str(" строке. На порядковом месте № ")+str(number[n1]))
print("2) Заданное число находится в "+str(n2)+str(" строке."))