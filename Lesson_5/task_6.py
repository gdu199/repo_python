# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
import os

def take_digits(my_str):
    result = ''
    for el in my_str:
        if el.isdigit():
            result += el
    if result == '':
        return 0
    else:
        return int(result)

def summator(var_list):
    result = 0
    for el in var_list:
        result += take_digits(el)
    return result

file_path = os.path.join(os.path.dirname(__file__), 'input_6.txt')

with open(file_path, 'r', encoding='UTF-8') as file:
    my_line_list = file.readlines()
my_list = [itm.split() for itm in my_line_list]

print(*my_list)

new_list = []

for itm in my_list:
    if len(itm) == 0:
        continue
    new_list.append((itm[0], summator(itm)))

my_dict = dict(new_list)

print(my_dict)

# Решение преподавателя
db = os.path.join(os.path.dirname(__file__), 'input_6.txt')
db_dict = {}
with open(db, 'r', encoding='UTF-8') as file:
    for line in file:
        tmp = line.split(' ')
        name = tmp[0].split(':')[0]
        db_dict[name] = tmp[1:]

result = {}
for key, value in db_dict.items():
    result[key] = sum([int(itm.split('(')[0]) for itm in value if itm.split('(')[0].isdigit()])
print('new', result)

