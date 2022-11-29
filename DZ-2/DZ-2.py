# 2) Требуется найти наименьший натуральный делитель 
# целого числа N, отличный от 1.
# Пример:
# Для n = 15: Ответ: 3
# Для n = 35: Ответ: 5

user_number = int(input('Input number:\n'))
div_range = abs(user_number) + 1

if user_number in [-1, 0, 1]:
    print(f'Minimum divider of number {user_number} is 1.')
else:
    for i in range(2, div_range):
        if user_number % i == 0:
            print(f'Minimum divider of number {user_number} is {i}.')
            break
