def int_func(var_str:str) -> str:
    if len(var_str) == 0:
        return var_str
    new_str = var_str[0].upper() + var_str[1:]
    return new_str

def int_func2(var_str: str) -> str:
    return var_str[0].upper() + var_str[1:] if var_str else var_str #''.join(

def user_temp(string: str):
    return ' '.join(map(int_func2, string.split(' ')))

var_str = input('Введите строку из слов, разделенных пробелом в нижнем регистре.\n').strip()
print(user_temp(var_str))
# my_list = var_str.split(' ')
# new_str = ''
# for el in my_list:
#     new_str = new_str + int_func2(el) + ' '
#
# print(new_str.strip())
