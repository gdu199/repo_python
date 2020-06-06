class Cells:

    def __init__(self, count):
        self.cell_count = count

    def __add__(self, other):
        return Cells(self.cell_count + other.cell_count)

    def __sub__(self, other):
        if self.cell_count > other.cell_count:
            return Cells(self.cell_count - other.cell_count)
        else:
            print('Количество клеток не положительное!')
            return None

    def __mul__(self, other):
        return Cells(self.cell_count * other.cell_count)

    def __truediv__(self, other):
        new_count = round(self.cell_count / other.cell_count)
        if new_count > 0:
            return Cells(new_count)
        else:
            print('Количество клеток не положительное!')
            return None

    def make_order(self, count_in_row):
        row_count = self.cell_count // count_in_row
        remainder = self.cell_count % count_in_row
        result = ''
        for i in range(row_count):
            result += '*' * count_in_row + '\n'
        result += '*' * remainder

        return result

var_cells_1 = Cells(10)
print(var_cells_1.make_order(4))

print('\n')

var_cells_2 = Cells(5)
print(var_cells_2.make_order(4))

print('\n')

var_cells = var_cells_1 - var_cells_2
print(var_cells.make_order(3))