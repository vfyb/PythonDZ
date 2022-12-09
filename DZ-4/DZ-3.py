# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.
# (Вывод тех элементов, которые были без повторов)
# Ввод: 1 2 3 2 4 4
# Вывод: 1 3


user_list_str = list(map(int, input('Input numbers divided with space: \n').split()))
result_list = []

for elem in user_list_str:
    if elem not in result_list:
        result_list.append(elem)

print(f'Not repeated elements in list: \n{user_list_str} => {result_list}')