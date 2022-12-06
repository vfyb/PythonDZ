# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

user_list1 = [2, 3, 4, 5, 6]
user_list2 = [2, 3, 5, 6]


def GetMultPairNumber(list):
    result_list = []
    
    for i in range(round((len(list) + 1) / 2)):
        result_list.append(list[i] * list[-i - 1])

    return result_list

print(f'{user_list1} =>', end =" ")
print(GetMultPairNumber(user_list1))

print(f'{user_list2} =>', end =" ")
print(GetMultPairNumber(user_list2))
