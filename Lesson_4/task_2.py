import random

def get_random_numbers(n):
    var_list = []
    for i in range(n):
        #var_list.append(random.random())
        var_list.append(random.randint(0,1000))
    return var_list

random_list = get_random_numbers(10)
print(random_list)

if len(random_list) == 0:
    exit()

new_list = []
previous = random_list[0]
for el in random_list:
    if el > previous:
        new_list.append(el)
    previous = el
print(new_list)

# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

print([*[itm for itm in range(21, 241, 21)], *[itm for itm in range(20, 241, 20)]])

#решение преподавателя
def test_iter(*args):
    prev = float('inf')
    for num in args:
        if num > prev:
            yield num
        prev = num


test = [-1, 4, 5, 3, 10, 2]
result = [itm for idx, itm in enumerate(test) if idx and itm > test[idx - 1]]
print(result)
