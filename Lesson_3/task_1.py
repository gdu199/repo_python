def my_division(num:float, denom:float) -> float:
    return num if not denom else num / denom

while True:
    user_value = input('Введите числитель\n')
    try:
        num = float(user_value)
    except ValueError as e:
        print(f"{e}\nНеверное значение данных")
        continue
    break

while True:
    user_value = input('Введите знаменатель\n')
    try:
        denom = float(user_value)
    except ValueError as e:
        print(f"{e}\nНеверное значение данных")
        continue
    break

print(my_division(num, denom))
