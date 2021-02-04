# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# Призначении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    speed = float
    color = str
    name = str
    is_police = bool

    def go(self):
        return print('Машина поехала!')

    def stop(self):
        return print('Машина остановилась!')

    def turn(self, direction):
        return print(f'Машина повернула в направлении {direction}')

    def show_speed(self):
        return self.speed

class TownCar(Car):
    speed = 70
    color = 'blue'
    name = 'bus'
    is_police = False

    def show_speed(self):
        if self.speed > 60:
            return print(f'Ваша скорость больше 60 км/час, аж {self.speed} км/час!')

class SportCar(Car):
    speed = 30
    color = 'red'
    name = 'bike'
    is_police = False

class WorkCar(Car):
    speed = 50
    color = 'yellow'
    name = 'taxi'
    is_police = False

    def show_speed(self):
        if self.speed > 40:
            return print(f'Ваша скорость больше 40 км/час, аж {self.speed} км/час!')

class PoliceCar(Car):
    speed = 100
    color = 'black'
    name = 'police'
    is_police = True


bus46 = TownCar()
merida = SportCar()
uber = WorkCar()
omon = PoliceCar()


