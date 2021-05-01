#!/usr/bin/env bash

# ${arr[*]} # Все записи в массиве
# ${!arr[*]}# Все индексы в массиве
# ${#arr[*]}# Количество записей в массиве
# ${#arr[0]}# Длина первой записи (нумерация с нуля)

array=(один яблоко Ваня автомобиль Москва [6]=музей)

echo "Записи в массиве: ${array[*]}"

echo "Индексы в массиве: ${!array[*]}"

echo "Количество записей: ${#array[*]}"

echo "Длина первой записи: ${#array[0]}"

echo "Пример: перебор массива циклом for"
 for i in ${array[*]}
 do
   printf "%s\n" $i
 done