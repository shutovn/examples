# Считая, что Земля – идеальная сфера с радиусом
# R ≈ 6350 км, определить расстояние до линии горизонта от точки с заданной высотой над Землей.

import math

R = 6350
# высоту надо вводить в км. 1 = км, а 0.001 = 1 метр
h = float(input("Введите заданую высоту в км: "))

# расчитываем расстояние из формулы S = sqrt( (R + h)**2 - R**2 )
S = math.sqrt( (R + h)**2 - R**2 )

# В выводе ограничеваем результат расчета 3 знаками после точки.
print ("Расстояние до линии горизонта от заданной точки = " + str(round(S, 3)) + " км.")