# Известна стоимость монитора, системного блока, клавиа­туры и мыши.
# Сколько будут стоить 3 компьютера из этих элементов? N компьютеров?

monitor = 8000
unit = 15000
keyboard = 1500
mouse = 300

amount = int(input("Введите кол-во компьюеров: "))

order = (monitor + unit + keyboard + mouse)

print ("При стоимости монитора " + str(monitor) + str(" руб."))
print ("При стоимости системного блока " + str(unit) + str(" руб."))
print ("При стоимости клавиатуры " + str(keyboard) + str(" руб."))
print ("При стоимости мышки " + str(mouse) + str(" руб."))
print ("3 комплекта будет стоить = " + str(3 * order) + str(" руб."))
print ( "Cтоимость " + str(amount) + " комп. будет равна = " + str(amount * order) + str(" руб."))
