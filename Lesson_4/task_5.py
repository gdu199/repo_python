# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

import sys
from itertools import count
from itertools import cycle

def my_iterator(n):
    quantity = 10
    i = 0;
    for el in count(n):
        if i >= quantity:
            break
        else:
            i += 1
            yield el

def my_cycle(n):
    i = 0
    for el in cycle(('ААА', 'ООО', 'ЕЕЕ')):
        if i >= n:
            break
        else:
            yield el
            i += 1


####################################################
_, *vars = sys.argv
if len(vars) == 0:
    print('Аргументов должно быть не меньше 1')
    exit()
n = vars[0]
if not n.isdigit():
    print('Тип аргумента должен быть числовым!')
    exit()

my_list = [itm for itm in my_iterator(int(n))]
print(my_list)

my_list = [itm for itm in my_cycle(int(n))]
print(my_list)
