# Создайте программу для игры в ""Крестики-нолики"".
# Ходить нужны выбирая цифру:
# 
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
# gamer(0) - X, gamer(1) - O

game_stage = {1: '1', 2: '2', 3: '3', 
              4: '4', 5: '5', 6: '6', 
              7: '7', 8: '8', 9: '9'}

win_comb = [[1,2,3], [4,5,6], [7,8,9],
            [1,4,7], [2,5,8], [3,6,9],
            [1,5,9], [3,5,7]]


def print_game_field(game_stage):
    for i in range(0, 7, 3):
        print('-' * 13)
        print(f'| {game_stage[1 + i]} | {game_stage[2 + i]} | {game_stage[3 + i]} |')
    
    print('-' * 13)


def gamer_input(gamer):
    
    if gamer == 0: cnange_cell = 'X'
    else: cnange_cell = 'O'

    flag = False
    while not flag:
        try:
            input_num = int(input(f'Gamer "{cnange_cell}":\nInput number from 1 to 9:\n'))
        except:
            print('Incorrect input. Try again.\n')
            continue
    
        if (input_num in range(1, 10)) and (game_stage[input_num] not in 'XO'):
            game_stage[input_num] = cnange_cell
            flag = True
        else:
            print('Choose another cell.')
            gamer_input(gamer)
    
    return game_stage


def check_for_win(game_stage):
    win_flag = False

    for i in win_comb:
        if (game_stage[i[0]] == game_stage[i[1]] == game_stage[i[2]]):
            win_flag = True
            break
        
    return win_flag

print_game_field(game_stage)

for i in range(9):
    gamer_input(i % 2)
    print_game_field(game_stage)
    
    if check_for_win(game_stage) == True:
        if i % 2 == 0:
            print('Gamer "X" is WIN!')
            break
        else:
            print('Gamer "O" is WIN!')
            break
    
    if (i == 8) and (check_for_win(game_stage) == False):
        print('Nobody win.')
        break

    continue
    
    

    

    