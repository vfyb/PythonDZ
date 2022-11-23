# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

user_number = int(input("Input number:\n"))

if user_number == 6 or user_number == 7:
    print('This day is weekend')
else:
    print('This day is workday')