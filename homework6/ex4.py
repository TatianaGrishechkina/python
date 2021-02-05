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
        return print(f'Машина повернула {direction}')

    def show_speed(self):
        return self.speed

class TownCar(Car):
    speed = 70
    color = 'синий'
    name = 'автобус'
    is_police = False

    def show_speed(self):
        if self.speed > 60:
            return print(f'Ваша скорость больше 60 км/час, аж {self.speed} км/час!')

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
            return print(f'Ваша скорость больше 40 км/час, аж {self.speed} км/час!')

class PoliceCar(Car):
    speed = 100
    color = 'черный'
    name = 'полиция'
    is_police = True


bus46 = TownCar()
merida = SportCar()
uber = WorkCar()
omon = PoliceCar()

print(f'Наш городской транспорт - это {bus46.name}. '
      f'Преобладающий цвет раскраски: {bus46.color}.'
      f'Несется со скоростью {bus46.show_speed()}, а теперь и вовсе {bus46.stop()}')

print(f'Наш спорт транспорт - это {merida.name}. '
      f'Преобладающий цвет раскраски: {merida.color}.'
      f'Несется со скоростью {merida.speed}')

print(f'Наш транспорт для поездок в офис - это {uber.name}. '
      f'Преобладающий цвет раскраски: {uber.color}.'
      f'Несется со скоростью {uber.show_speed()}')

print(f'А вот это - {omon.name}. '
      f'Преобладающий цвет раскраски: {omon.color}.'
      f'Несется со скоростью {omon.speed}.'
      f'Машина {uber.turn(direction="налево")}')
