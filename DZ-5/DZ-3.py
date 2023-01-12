# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"
# Восстановить
# Ввёл: stroka = "3a4b2c3b"
# Вывод: stroka = "aaabbbbccbbb"

def compress(text):
    if len(text) < 1:
        return ''
    # Эта строка появилась если подряд запускать прогу 
    # и в итоге в файле к первой строке дописывается \n в конце и ломает все.
    # Если запускать первый раз, то все работает, но потом ломается...
    text = text.replace('\n', '')
    
    letter = text[0]
    count = 0
    result = ''

    for elem in text:
        if elem == letter:
            count += 1
        else:
            result += str(count) + letter
            letter = elem
            count = 1
    result += str(count) + letter
    
    return result

def decompress(text):
    if len(text) < 1:
        return ''
    
    text = text.replace('\n', '')
    result = ''
    digit = ''

    for elem in text:
        if elem.isdigit():
            digit += elem
        else:
            for i in range(int(digit)):
                result += elem
            digit = ''
    
    return result
    
path_decomp = 'DZ-5/DZ-3-1.txt'
path_comp = 'DZ-5/DZ-3-2.txt'

# Компрессиия стройки из файла
str_decomp = open(path_decomp, 'r')
text_compressed = compress(str_decomp.readline())
print(text_compressed)
str_decomp.close()

data = open(path_comp, 'a')
data.write(f'\n{text_compressed}')
data.close()

# Декомпрессия строки из файла
str_comp = open(path_comp, 'r')
text_decompressed = decompress(str_comp.readline())
print(text_decompressed)
str_comp.close()

data = open(path_decomp, 'a')
data.write(f'\n{text_decompressed}')
data.close()












