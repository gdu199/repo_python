def my_userinfo(**kwargs):
    info = ''
    for key, value in kwargs.items():
        info += f'{key} : {value}; '
    return info

print(my_userinfo(name = 'bob', surname = 'marly'))