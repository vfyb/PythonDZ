# Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

user_list = [4, 7, -3, 9, 6, -54, 67, 8]

def GetSumOddElements(list):
    sum_odd = 0
    for i in range(1, len(list), 2):
        sum_odd += list[i]
    return sum_odd

print(f'Sum of odd elements in {user_list} = {GetSumOddElements(user_list)}')