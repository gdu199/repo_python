stop_run = False
var_sum = 0
while not stop_run:
    while True:
        var_str = input('Введите числа через пробел. Для окончания ввода, введите "q"\n').strip()
        my_list = var_str.split(' ')
        #print('список: ', my_list)
        if 'q' in my_list:
            stop_run = True
            ind_q = my_list.index('q')
            my_list.pop(ind_q)
        try:
            new_list = list(map(int, my_list))
        except ValueError as e:
            print(f"{e}\nНеверное значение данных")
            continue
        break
    var_sum += sum(new_list)
    print('Сумма введенных чисел: ', var_sum)