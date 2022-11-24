# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

x1 = int(input('Input X oordinate for first point:\n'))
y1 = int(input('Input Y oordinate for first point:\n'))

x2 = int(input('Input X oordinate for second point:\n'))
y2 = int(input('Input Y oordinate for second point:\n'))

# round сделал до 3 знаков, иначе для 1 примера округляет до 5,1 (что в общем-то верно)
distance = round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 3)
print(f'Distance between points A({x1, y1}) and B({x2, y2}) = {distance}')
