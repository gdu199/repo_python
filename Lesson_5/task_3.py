# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
import os

file_path = os.path.join(os.path.dirname(__file__), 'input_3.txt')

file = open(file_path, 'r', encoding='UTF-8')
line_list = file.readlines()

total_salary = 0
employee_count = 0
for line in line_list:
    word_list = line.split()
    if len(word_list) == 0:
        break
    try:
        salary = float(word_list[1])
    except ValueError as error:
        print(f'Невозможно определить зарплату сотрудника: {word_list[0]}')
        print(error)
        continue
    if salary < 20000:
        print(f'У сотрудника {word_list[0]} зарплата менее 20000 $')
    total_salary += salary
    employee_count += 1

print(f'Средняя зарплата сотрудников составляет {round(total_salary/employee_count, 2): .2f}')

file.close()