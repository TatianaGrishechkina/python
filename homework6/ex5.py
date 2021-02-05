# 5. Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
from ex4 import *

bus46 = TownCar()
merida = SportCar()
uber = WorkCar()
omon = PoliceCar()

print(f'Наш городской транспорт - это {bus46.name}. '
      f'Преобладающий цвет раскраски: {bus46.color}.')
bus46.show_speed()

print(f'Наш спорт транспорт - это {merida.name}. '
      f'Преобладающий цвет раскраски: {merida.color}.')
merida.show_speed()

print(f'Наш транспорт для поездок в офис - это {uber.name}. '
      f'Преобладающий цвет раскраски: {uber.color}.')
uber.show_speed()
uber.turn(direction="налево")

print(f'А вот это - {omon.name}. '
      f'Преобладающий цвет раскраски: {omon.color}.')
omon.show_speed()
omon.stop()

