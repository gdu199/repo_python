# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MonthCountError(Exception):
	def __init__(self, text=''):
		self.text = text

class My_Income:

    def __init__(self, income, month_count):
        self.income = income
        self.month_count = month_count

    def incom_per_month(self):
        if type(self.month_count) == int and self.month_count > 0:
            return round(self.income / self.month_count, 2)
        else:
            raise MonthCountError('Ошибка в объекте. Количество месяцев должно быть > 0')

if __name__ == '__main__':
    last_year = My_Income(1000000, 0)
    try:
        print('Доход в месяц составил: ', last_year.incom_per_month())
    except MonthCountError as e:
        print(e)