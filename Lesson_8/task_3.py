# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
# введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.

class InputNumberError(Exception):
	def __init__(self, text=''):
		self.text = text

class My_List:
    def __init__(self):
        self.data = []

    def add_element(self, el):
        if el.isdigit():
            self.data.append(int(el))
        else:
            raise InputNumberError('Введено не число!')

    def __str__(self):
        return str(self.data)

if __name__ == '__main__':
    var_list = My_List()
    while True:
        tmp = input('Введите числовой элемент списка\n')
        if tmp == 'stop':
            break
        try:
            var_list.add_element(tmp)
        except InputNumberError as e:
            print(e)
    print(var_list)