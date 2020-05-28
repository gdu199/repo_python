import sys

def payroll(var_list):
    if len(var_list) < 3:
        print('Аргументов должно быть не меньше 3')
        return
    try:
        salary = float(var_list[0]) * float(var_list[1]) + float(var_list[2])
        print(f'Расчет зарплаты: {salary:.2f} рублей')
    except ValueError as e:
        print("Аргументы должны быть числовые")
        print(e)
        return


# print(sys.argv)
_, *vars = sys.argv

# можно вот так.
# _, hour, price, bonus, *__ = argv
#__ принимает в себя остальные параметры как список

payroll(vars)
