def int_func(var_str:str) -> str:
    if len(var_str) == 0:
        return var_str
    new_str = var_str[0].upper() + var_str[1:]
    return new_str

print(int_func('text'))

var_str = input('Введите строку из слов, разделенных пробелом в нижнем регистре.\n').strip()
my_list = var_str.split(' ')
new_str = ''
for el in my_list:
    new_str = new_str + int_func(el) + ' '

print(new_str.strip())
