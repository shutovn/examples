# В кинотеатре имеется 20 рядов мест для зрителей, в каждом из которых расположено 15 кресел.
# Билет для зрителей имеет серию АВ и номер билета, для первого места в первом ряду
# равного 01643 (далее этот номер увеличивается согласно условному обозначению мест,
# имеющему вид, показанный в таблице ниже):
#
#   |  1  |  2  | ... | 15  |
#   | 16  | 17  | ... | 30  |
#   | ... | ... | ... | ... |
#   | 286 | 287 | ... | 300 |
#
# Определить, в каком ряду находится место, билет на которое
# имеет заданный серийный номер.

import math

print ("Билет для зрителей имеет серию АВ и № 01643, для первого места в первом ряду.")
print ("Номера билетов в зале находятся в диапозоне от 01643 до 01943")
n = int(input("Введите № билета: "))

if ( n < 1643 ) or ( n > 1943 ):
    print ("Номер вашего билета 0"+str(n)+str(" и он из другого зала."))
else:
    s = n - 1643
    r = math.ceil(s / 15)
    print ("Номер введенного билета соответствует "+str(s)+str(" месту и находится в ")+str(r)+str(" ряду."))
