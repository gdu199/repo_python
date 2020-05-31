# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
import os

file_path = os.path.join(os.path.dirname(__file__), 'input_2.txt')

file = open(file_path, 'r', encoding='UTF-8')
line_list = file.readlines()
print('Количество строк в файле: ', len(line_list))

for str_numb, line in enumerate(line_list):
    word_list = (line.split())
    print(f'В строке {str_numb+1} количество слов: ', len(word_list))

file.close()