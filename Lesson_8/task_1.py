# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

import datetime

class MyDate:

    cls_str_date = ''

    def __init__(self, str_date):
        self.str_date = str_date
        MyDate.cls_str_date = str_date

    @staticmethod
    def validate_date(str_date):
        var_list = str_date.split('-')
        if len(var_list) < 3 or not var_list[0].isdigit() or len(var_list[0]) != 2 \
        or not var_list[1].isdigit() or len(var_list[1]) != 2 \
        or not var_list[2].isdigit() or len(var_list[2]) != 4:
            print('Строка должа быть в формате ДД-ММ-ГГГГ')
            return None
        dd, mm, yyyy = int(var_list[0]), int(var_list[1]), int(var_list[2])
        try:
            var_date = datetime.date(yyyy, mm, dd)
            return (dd, mm, yyyy)
        except ValueError as e:
            print(e)
            return None


    @classmethod
    def get_numbers(cls):
        var_tuple = cls.validate_date(cls.cls_str_date)
        return var_tuple


a = MyDate('32-06-2020')
print(a.get_numbers())