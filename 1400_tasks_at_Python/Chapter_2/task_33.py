# Возраст Тани – X лет, а возраст Мити – Y лет.
# Найти их средний возраст, а также определить,
# на сколько отличается возраст каждого ребенка от среднего значения.
import math

x = int(input("Введите возраст Тани: "))
y = int(input("Введите возраст Мити: "))

a = (x + y)/2

s = math.fabs(x - a)

print ("Средний возраст детей = " + str(a) )
print ("Возраст Тани отличается от среднего на " +str(s))
print ("Возраст Мити отличается от среднего на " +str(s))
