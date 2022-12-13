# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# (или вывести в терминал) многочлен степени k.
# Пример:
# - k = 2  => 2*x² + 4*x + 5
# - k = 3  => 41*x^3 + 6*x² + 2*x + 98

from random import randint

k = int(input('Input the natural degree of a polynomial:\n'))
polynomial = ''

def random_ratio_x(i):
    result = ''
    
    if i == 0:
        result = str(randint(0, 101))
    elif i == 1:
        result = str(randint(0, 101)) + '*x' + ' + '
    else:
        result = str(randint(0, 101)) + '*x^' + str(i) + ' + '

    return (result)

for i in range(0, k + 1):
    polynomial = str(random_ratio_x(i)) + polynomial

print(f'k={k} => {polynomial}')

with open('DZ-4.txt', 'w') as data:
    data.write(f'k = {k} => {polynomial} \n')