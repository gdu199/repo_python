class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}*i'

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return ComplexNumber(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        # (a + bi) * (c + di) = (ac - bd) + (bc + ad)*i
        return ComplexNumber(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

if __name__ == '__main__':

    a = 1
    b = 2
    c = 3
    d = 4
    ab = ComplexNumber(a,b)
    cd = ComplexNumber(c,d)

    print(ab + cd)
    print(ab * cd)