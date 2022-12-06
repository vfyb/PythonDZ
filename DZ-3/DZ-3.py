# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

user_list1 = [1.1, 1.2, 3.1, 5, 10.01]
user_list2 = [1.67, 1.55, 3.987, 5, 10.34]

def GetDiffMaxMin(list):
    fractional_part_list =[]

    for i in range(len(list)):
        if (list[i] % 1) != 0:
            fractional_part_list.append(round((list[i] % 1), 3))

    print(fractional_part_list)
    return(round(( max(fractional_part_list) - min(fractional_part_list) ), 3))

print(GetDiffMaxMin(user_list1))
print(GetDiffMaxMin(user_list2))
