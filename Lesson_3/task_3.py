def my_func(var_1, var_2 , var_3):
    my_list = [var_1, var_2, var_3]
    var_min = min(my_list)
    my_list.pop(my_list.index(var_min))
    print(my_list)
    return sum(my_list)

print(my_func(1, 2, 3))