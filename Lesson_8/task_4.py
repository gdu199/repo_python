# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Office_Equipment:
    def __init__(self, brand, article_number, cost):
        self.brand = brand
        self.article_number = article_number
        self.cost = cost

class Printer(Office_Equipment):
    def __init__(self, printer_type, color_printer, *args, **kwargs):
        super().__init__()
        self.printer_type = printer_type
        self.color_printer = color_printer

class Scanner(Office_Equipment):
    def __init__(self, scanner_type, scan_size, *args, **kwargs):
        super().__init__()
        self.scanner_type = scanner_type
        self.scan_size = scan_size

class Xerox(Office_Equipment):
    def __init__(self, xerox_size, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.xerox_size = xerox_size
        self.model = model

    def __str__(self):
        return f'Ксерокс {self.brand} {self.model}. Артикул: {self.article_number}, стоимость: {self.cost} руб'

if __name__ == '__main__':
    my_equp_25 = Xerox('A4', 'b-52', 'HP', 25, 12000)
    print(my_equp_25)

