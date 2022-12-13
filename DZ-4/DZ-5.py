# Дополнительное Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# Файл1: 2*x^2 + 4*x + 5
# Файл2: 41*x^3 + 6*x^2 + 2*x + 98
# Вывод Файл3: 41*x^3 + 8*x^2 + 6*x + 103

def get_data_from_file(path):
    with open(path, 'r') as file:
        string_from_file = file.readline() + '*x^0'
        dict_from_file = dict(sub_elem.split('*') for sub_elem in string_from_file.split(' + '))
        dict_from_file = {v: k for k, v in dict_from_file.items()}
    return dict_from_file

dict_from_1_file = get_data_from_file('DZ-4/DZ-5-1.txt')
dict_from_2_file = get_data_from_file('DZ-4/DZ-5-2.txt')

if len(dict_from_1_file) >= len(dict_from_2_file):
    max_dict = dict_from_1_file
else:
    max_dict = dict_from_2_file

dict_result = {}

for key in max_dict:
    if (key in dict_from_1_file) & (key in dict_from_2_file):
        dict_result[key] = str(int(dict_from_1_file[key]) + int(dict_from_2_file[key]))
    elif (key in dict_from_1_file) & (key not in dict_from_2_file):
        dict_result[key] = dict_from_1_file[key]
    elif (key not in dict_from_1_file) & (key in dict_from_2_file):
        dict_result[key] = dict_from_2_file[key]

def create_polinom(dict):
    result = ''
    for key in dict:
        if key != 'x^0':
            result = result + dict[key] + '*' + key + ' + '
        else:
            result = result + dict[key]
    return result

print(f'{create_polinom(dict_from_1_file)} \n + \n{create_polinom(dict_from_2_file)} \n = \n{create_polinom(dict_result)}')

with open('DZ-4/DZ-5-3.txt', 'w') as data:
    data.write(create_polinom(dict_result))