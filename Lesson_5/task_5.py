# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random
import os


def get_random_numbers(n):
    var_list = []
    for i in range(n):
        var_list.append(str(random.randint(0,1000)))
    return var_list

def get_sum(my_list):
    return(sum(map(int, my_list)))

#строка случайных чисел
my_str = " ".join(get_random_numbers(3))
print(my_str)

file_path = os.path.join(os.path.dirname(__file__), 'output_5.txt')

with open(file_path, 'w') as file:
    file.write(my_str)

#читаем из файла
with open(file_path, 'r') as file:
    my_line_list = file.readlines()
my_list = [itm.split() for itm in my_line_list]
print(*my_list)

#вычисляем сумму
print(get_sum(*my_list))

# Решение преподавателя
to_file_numbers = [random.randint(1, 200) for _ in range(random.randint(10, 250))]
# то есть размер списка тоже выбирается случайно
