# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет. 
# Победитель - тот, кто оставил на столе 0 конфет.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# 2021 21 ---> 2000 бот4 -> 1996 .... бот --->29 --> 27 >> 2конф
# a) Добавьте игру против бота
# # Доп b) Подумайте как наделить бота "интеллектом" (Теория игр)

from random import randint

game_status = 120
print(f'\nYou see {game_status} candies and can take 28 or less of them.\nInput number how many candies you will take.\n')

def gamer_input(max):
    flag = False
    while not flag:
        try:
            input_num = int(input(f'Input number from 1 to {max}:\n')) 
            flag = True
        except:
            print(f'Incorrect input, try again with number from 1 to {max}.')
            continue
    return input_num

def human_gamer(game_status):
    max = 28 if game_status >= 28 else game_status
    
    num_flag = False
    while not num_flag:
        input_num = gamer_input(max)
    
        if input_num <= max:
            game_status = game_status - input_num
            num_flag = True
            return game_status
            
        elif (input_num <= max) and (game_status < 28):
            print(f'There are only {game_status} candies. Input number from 1 to {game_status}.')
            continue
        elif input_num not in range(1, 29):
            print('Your number is not in range from 1 to 28. Try again.\n')
            continue
    

def bot_gamer(game_status):
#  Немного интеллекта добавил )
    if game_status in range(30, 58): # 57 = 28 + 29. Надо оставить второму игроку 29, после чего любой ход второго игрока приведет его к проигрышу
        comp_num = game_status - 28 - 1
    elif game_status in range(1, 29): comp_num = game_status
    else: comp_num = randint(1, 28)
    
    print(f'Computer number is:\n{comp_num}')
    return game_status - comp_num

while game_status > 0:
    game_status = human_gamer(game_status)

    if game_status == 0:
        print('Congratulations! You win!\n')
        break
    else:
        print(f'\nThere are {game_status} candies now.\n')

    game_status = bot_gamer(game_status)

    if game_status == 0:
        print('Computer win!\n')
        break
    else:
        print(f'\nThere are {game_status} candies now.\n')
        