# 4)Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

user_number = int(input('Input number:\n'))

user_range = abs(user_number)
sum_even_numbers = 0

for i in range(2, user_range + 1, 2):
    sum_even_numbers += i

if user_number > 0:
    print(f'Sum of even numbers from 1 to {user_number} = {sum_even_numbers}.')
else:
    print(f'Sum of even numbers from 1 to {user_number} = {-sum_even_numbers}.')
