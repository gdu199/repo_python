def my_func(x: float, y:int):
    return x ** y

def my_func_2(x: float, y:int):
    if y > 0:
        return x
    if x == 0:
        return x

    result = 1
    for i in range(y, 0):
        result /= x
    return result


print(my_func(2, -5))
print(my_func_2(2, -5))