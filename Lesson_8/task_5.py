# попытка учета в разрезе склада

class CountError(Exception):
	def __init__(self, text=''):
		self.text = text

class ArticleNumberError(Exception):
	def __init__(self, text=''):
		self.text = text

class Office_Equipment:
    elements = {}

    @classmethod
    def get_element(cls, article_number):
        if article_number in cls.elements:
            return cls.elements[article_number]
        return False

    def __init__(self, brand, article_number, cost):
        self.brand = brand
        self.article_number = article_number
        self.cost = cost

class Printer(Office_Equipment):
    def __init__(self, printer_type, color_printer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        el = Office_Equipment.get_element(self.article_number)
        if el:
            if type(el) == Printer:
                self = el
            else:
                raise ArticleNumberError(f'Артикул {self.article_number} принадлежит другому типу оборудовния')
        else:
            Office_Equipment.elements.setdefault(self.article_number, self)
        self.printer_type = printer_type
        self.color_printer = color_printer
    def __str__(self):
        return f'Принтер {self.brand}. Артикул: {self.article_number}'

class Scanner(Office_Equipment):
    def __init__(self, scanner_type, scan_size, *args, **kwargs):
        super().__init__(*args, **kwargs)
        el = Office_Equipment.get_element(self.article_number)
        if el:
            if type(el) == Scanner:
                self = el
            else:
                raise ArticleNumberError(f'Артикул {self.article_number} принадлежит другому типу оборудовния')
        else:
            Office_Equipment.elements.setdefault(self.article_number, self)
        self.scanner_type = scanner_type
        self.scan_size = scan_size
    def __str__(self):
        return f'Сканер {self.brand}. Артикул: {self.article_number}'

class Xerox(Office_Equipment):
    def __init__(self, xerox_size, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        el = Office_Equipment.get_element(self.article_number)
        if el:
            if type(el) == Xerox:
                self = el
            else:
                raise ArticleNumberError(f'Артикул {self.article_number} принадлежит другому типу оборудовния')
        else:
            Office_Equipment.elements.setdefault(self.article_number, self)
        self.xerox_size = xerox_size
        self.model = model
    def __str__(self):
        return f'Ксерокс {self.brand} {self.model}. Артикул: {self.article_number}, стоимость: {self.cost} руб'


class WareHouse:
    def __init__(self):
        # self.data = {'Артикул1':  (printer1, {'Склад1': 5, 'Подразделение1': 7 } ),
        #              'Артикул2':  (printer2, {'Подразделение1': 6, })
        #              }
        self.data = {}
        self.division1 = "Склад"

    def get_equip_info(self, article_number):
        equip = Office_Equipment.get_element(article_number)
        if not equip:
            raise ArticleNumberError(f'Не найдено оборудование с артикулом {article_number}')

        if not article_number in self.data:
            self.data[article_number] = (equip, {self.division1: 0})
        return self.data[article_number]

    def do_entrance(self, article_number, count):
        if type(count) != int:
            raise CountError('Количество должно быть целым числом')
        eq_inf = self.get_equip_info(article_number)
        eq_inf[1][self.division1] += count

    def do_shipment(self, article_number, target_division, count):
        if type(count) != int:
            raise CountError('Количество должно быть целым числом')
        eq_inf = self.get_equip_info(article_number)
        if eq_inf[1][self.division1] < count:
            raise CountError(f'На складе недостаточно количества по артикулу {article_number}')
        eq_inf[1][self.division1] -= count
        if target_division in eq_inf[1]:
            eq_inf[1][target_division] += count
        else:
            eq_inf[1][target_division] = count

    def get_warehouse_balance(self):
        result = ''
        for itm in self.data.values():
            result += f'{str(itm[0])} {str(itm[1])}\n'
        return result

if __name__ == '__main__':

    my_ware_house = WareHouse()
    my_equp_25 = Printer('Laser', True, 'HP', 25, 12000)
    scan15 = Scanner('Планшет', 'A4', 'HP', 15, 10000)
    my_ware_house.do_entrance(25, 10)
    my_ware_house.do_shipment(25, 'Отдел продаж', 5)
    my_ware_house.do_entrance(15, 20)
    print(my_ware_house.get_warehouse_balance())

# class Division:
#     __elements = {}
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def get_division(cls, name):
#         for el in cls.__elements.items():
#             if el.name == name:
#                 return el
#         new_division = Division(name)
#         cls.__elements.add(new_division)
#         return new_division
