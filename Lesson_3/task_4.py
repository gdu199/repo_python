def my_func(x: float, y:int):
    return x ** y

def my_func_2(x: float, y:int):
    # if y > 0:
    #     return x
    if x == 0:
        return x

    result = 1
    for i in range(abs(y)):
        result *= x
    return result if y > 0 else 1/result


print(my_func(2, -5))
print(my_func_2(2, -5))