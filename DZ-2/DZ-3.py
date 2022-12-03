# 3) Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, 
# который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

index_spisok = [2, 2, 3, 1, 8]
user_number = abs(int(input('Input number:\n')))

user_list = list(range(-user_number, user_number + 1))
mult_result = 1

if max(index_spisok) > len(user_list):
    print('Cannot count multiplication.')
else:
    for index in index_spisok:
        mult_result *= user_list[index]
    print(f'Multiply = {mult_result}')
