# Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N.
# 24
# 2 2 2 3

# Сначала поставил диапазон чисел до корня из введенного числа (как везде пишут), 
# но это не работает!
# Например на числах меньше 16. А на числе 1902 не выдает 317.
# Решил сделать диапазон проверок в половину числа... + 1 конечно )

import math

user_number = int(input('Input number:\n'))
divide_nums = []

for i in range(2, int(user_number / 2) + 1):
    if (user_number % i == 0):
        while (user_number % i == 0) & (user_number > 1):
            divide_nums.append(i)
            user_number = user_number / i

if divide_nums == []:
    divide_nums.append(user_number)

print(divide_nums)
