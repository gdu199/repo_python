from abc import ABC, abstractmethod

class Clothes:
    def __init__(self, V, H):
        self.V = V
        self.H = H

    @abstractmethod
    def consaption(self):
        pass

class Coat(Clothes):

    def __init__(self, V):
        super().__init__(V, 0)

    @property
    def consaption(self):
        return f'Для пальто нужно {self.V / 6.5 + 0.5: 0.2f} ткани'

class Suit(Clothes):

    def __init__(self, H):
        super().__init__(0, H)

    @property
    def consaption(self):
        return f'Для костюма нужно {2 * self.H + 0.3} ткани'

suit_1 = Suit(5)
coat_1 = Coat(4)

print(suit_1.consaption)
print(coat_1.consaption)


