# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет. 
# Победитель - тот, кто оставил на столе 0 конфет.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# 2021 21 ---> 2000 бот4 -> 1996 .... бот --->29 --> 27 >> 2конф
# a) Добавьте игру против бота
# # Доп b) Подумайте как наделить бота "интеллектом" (Теория игр)

from random import randint

game_status = int(120)
print(f'You see {game_status} candies and can take 28 or less of them.\nInput number how many candies you will take')

def human_gamer(game_status):
    # Это условие для ввода корректных чисел когда конфет < 28
    if game_status in range(1, 28):
        input_num = int(input(f'Input number from 1 to {game_status}:\n'))
        
        if input_num in range(1, game_status + 1):
            return game_status - input_num
        else:
            print(f'Your number is not in range from 1 to {game_status}.\n')
            human_gamer(game_status)

    else:
        input_num = int(input('Input number from 1 to 28:\n'))

        if input_num in range(1, 29):
            return game_status - input_num
        else:
            print('Your number is not in range from 1 to 28.\n')
            human_gamer(game_status)

def bot_gamer(game_status):
#  Немного интеллекта добавил )
    if game_status in range(30, 58): # 57 = 28 + 29. Надо сотавить второму игроку 29, после чего любой ход второго игрока приведет его к проигрышу
        comp_num = game_status - 28 - 1
    elif game_status in range(1, 29): comp_num = game_status
    else: comp_num = randint(1, 28)
    
    print(f'Computer number is:\n{comp_num}')
    return game_status - comp_num

while game_status > 0:
    game_status = human_gamer(game_status)

    if game_status == 0:
        print('Congratulations! You win!')
        break
    else:
        print(f'There are {game_status} candies now')

    game_status = bot_gamer(game_status)

    if game_status == 0:
        print('Computer win!')
        break
    else:
        print(f'There are {game_status} candies now')
        