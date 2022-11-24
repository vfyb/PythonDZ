# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

user_number = int(input('Input number of quarter plane (1-4):\n'))

if user_number < 1 or user_number > 4:
    print('You entered wrong number.')
elif user_number == 1:
    print('Coordinate range: X > 0 and Y > 0')
elif user_number == 2:
    print('Coordinate range: X < 0 and Y > 0')
elif user_number == 3:
    print('Coordinate range: X < 0 and Y < 0')
else:
    print('Coordinate range: X > 0 and Y < 0')
