# 1) Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

user_number = int(input('Input number:\n'))
factorial = 1

if user_number < 0:
    print(f'Cannot find factorial of {user_number}.')
elif user_number == 0 or user_number == 1:
    print(f'Factorial of number {user_number} = {factorial}')
else:
    for i in range(2, user_number + 1):
        factorial = factorial * i
    print(f'Factorial of number {user_number} = {factorial}')
    