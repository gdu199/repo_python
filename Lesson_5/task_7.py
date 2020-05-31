#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# + Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# + Если фирма получила убытки, в расчет средней прибыли ее не включать.
# + Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
import json
import os

def get_number(var_str):
    try:
        result = float(var_str)
    except ValueError as error:
        result = 0
    return result

def calc_profit(itm):
    return get_number(itm[2]) - get_number(itm[3])

file_path = os.path.join(os.path.dirname(__file__), 'input_7.txt')

with open(file_path, 'r', encoding='UTF-8') as file:
    my_line_list = file.readlines()
my_list = [itm.split() for itm in my_line_list]
# print(*my_list)

# формирование структур данных
new_list = []
for itm in my_list:
    new_list.append((itm[0], calc_profit(itm)))
my_dict = dict(new_list)

# Расчет средней
profit_list = []
for itm in new_list:
    i_profit = itm[1]
    if i_profit >= 0:
        profit_list.append(i_profit)
if len(profit_list) == 0:
    average_profit = 0
else:
    average_profit = round(sum(profit_list)/len(profit_list), 2)
print('Средняя прибыль: ', average_profit)

# Формирование списка
var_list = [my_dict, dict([('average_profit', average_profit)])]
print(var_list)

# Вывод в файл
with open('J_data.json', 'w') as j_file:
    json.dump(var_list, j_file)
