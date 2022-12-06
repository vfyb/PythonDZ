# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

user_number = int(input('Input number:\n'))

def DecimalToBinary(number):
    binary = ''
    
    while number != 0:
        binary += str(number % 2)
        number = (number // 2)

    return(binary[::-1])

print(f'Number {user_number} in binary mode = {DecimalToBinary(user_number)}.')
print(f'To be sure, binary find with Python method: {bin(user_number)}.')