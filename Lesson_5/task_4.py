# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
import os

def translator(line):
    new_line = line
    new_line = new_line.replace('One', 'Один')
    new_line = new_line.replace('Two', 'Два')
    new_line = new_line.replace('Three', 'Три')
    new_line = new_line.replace('Four', 'Четыре')
    return new_line

file_path_input = os.path.join(os.path.dirname(__file__), 'input_4.txt')
file_path_output = os.path.join(os.path.dirname(__file__), 'output_4.txt')

with open(file_path_input, 'r', encoding='UTF-8') as file, open(file_path_output, 'w', encoding='UTF-8') as out_file:
    for line in file:
        out_file.write(translator(line))
print('Завершено')
