# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# Призначении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    speed = 0.0
    color = ''
    name = ''
    is_police = False

    def go(self):
        print('Машина поехала!')

    def stop(self):
        print('Машина остановилась!')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость: {self.speed} км/час.')


class TownCar(Car):
    speed = 70
    color = 'синий'
    name = 'автобус'
    is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'Ваша скорость больше 60 км/час, аж {self.speed} км/час!')
        else:
            print(f'Ваша скорость нормальная, {self.speed} км/час.')


class SportCar(Car):
    speed = 30
    color = 'красный'
    name = 'феррари'
    is_police = False


class WorkCar(Car):
    speed = 50
    color = 'желтый'
    name = 'такси'
    is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'Несется со скоростью больше 40 км/час, аж {self.speed} км/час!')
        else:
            print(f'Ваша скорость нормальная, {self.speed} км/час.')


class PoliceCar(Car):
    speed = 100
    color = 'черный'
    name = 'полиция'
    is_police = True

