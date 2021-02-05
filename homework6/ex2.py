# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина),
# width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта для покрытия одного
# кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _length = 0.0
    _width = 0.0

    def __init__(self, length_in_meters, width_in_meters):
        self._width = width_in_meters
        self._length = length_in_meters

    def calculate(self, asphalt_mass=25, height=5):
        return self._length * self._width * asphalt_mass * height / 1000


road = Road(length_in_meters=20, width_in_meters=5000)
print(f'Для покрытия дороги потребуется {road.calculate()} тонн асфальта.')
