# stop_run = False
# var_sum = 0
# while not stop_run:
#     while True:
#         var_str = input('Введите числа через пробел. Для окончания ввода, введите "q"\n').strip()
#         my_list = var_str.split(' ')
#         #print('список: ', my_list)
#         if 'q' in my_list:
#             stop_run = True
#             ind_q = my_list.index('q')
#             my_list.pop(ind_q)
#         try:
#             new_list = list(map(int, my_list))
#         except ValueError as e:
#             print(f"{e}\nНеверное значение данных")
#             continue
#         break
#     var_sum += sum(new_list)
#     print('Сумма введенных чисел: ', var_sum)

def insert_sum(*args):
    result = 0
    exit_flag = False
    for itm in args:
        try:
            result += float(itm) if itm else 0
        except ValueError as e:
            if itm == 'q':
                exit_flag = True
    return result, exit_flag

user_sum = 0
while True:
    user_input = input('Введите числа через пробел\n').split(' ')
    result_sum, user_exit = insert_sum(*user_input)
    user_sum += result_sum
    print(f'Сумма: {user_sum}')

    if user_exit:
        break