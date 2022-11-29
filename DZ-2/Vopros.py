# 1) Напишите программу, которая будет принимать на вход дробь 
# и показывать первую цифру дробной части числа.
# *Пример* 
# Ввод: 0,5
# Вывод: 5


user_str = input('Input number:\n')

def PrintFirstDigitAfterComma(user_str):
    user_number = float(user_str)
    print(user_number) # Для контроля
    print(user_number - int(user_number)) # Для контроля
    print(int((user_number - int(user_number)) * 10))

if ','in user_str:
    user_str = user_str.replace(',', '.')
    PrintFirstDigitAfterComma(user_str)

elif '.' in user_str:
    PrintFirstDigitAfterComma(user_str)

else:
    print('Not found')
