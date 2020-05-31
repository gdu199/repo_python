# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
import os

file_path = os.path.join(os.path.dirname(__file__), 'output_1.txt')

with open(file_path, 'w', encoding='UTF-8') as file:
    while True:
        var_str = input('Введите строку. Пустая строка означает завершение ввода\n')
        #if var_str.strip() == '':
        if not var_str:
            break
        file.write(var_str + '\n')
print('Ввод завершен')

