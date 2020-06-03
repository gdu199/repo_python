# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed = 0
    def __init__(self, is_police, color, name):
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self, speed):
        self.speed = speed
        print(f'{self.name} поехала')
    def stop(self):
        self.speed = 0
        print(f'{self.name} остановилась')
    def turn(self, direction):
        print(f'{self.name} повернула {direction}')
    def show_speed(self):
        print(f'Скорость автомобиля {self.name} составляет {self.speed}')

class TownCar(Car):
    def __init__(self, *args, **kwargs):
        is_police = False
        super().__init__(is_police, *args, **kwargs)

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости на {self.speed - 60}')
        else:
            print(f'Скорость автомобиля {self.name} составляет {self.speed}')

class WorkCar(Car):
    def __init__(self, *args, **kwargs):
        is_police = False
        super().__init__(is_police, *args, **kwargs)

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости на {self.speed - 40}')
        else:
            print(f'Скорость автомобиля {self.name} составляет {self.speed}')

class SportCar(Car):
    def __init__(self, *args, **kwargs):
        is_police = False
        super().__init__(is_police, *args, **kwargs)

class PoliceCar(Car):
    def __init__(self, *args, **kwargs):
        is_police = True
        super().__init__(is_police, *args, **kwargs)


car1 = TownCar('blue', 'ford')
car1.go(70)
car1.show_speed()
car1.stop()
car1.show_speed()

car7 = PoliceCar('black', 'chevrolet')
car7.go(120)
car7.show_speed()

car3 = SportCar('yellow', 'lamborgini')
car3.go(230)
car3.turn('left')
print(car3.color, car3.name)
