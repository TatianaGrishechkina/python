# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
# соответствующее сообщение и завершать скрипт.
import time


class TrafficLight:
    def __init__(self):
        self.__color_tl = 'зеленый'

    def running(self):
        if self.__color_tl == 'зеленый':
            self.__color_tl = 'красный'
            print(f'На светофоре {self.__color_tl} цвет.')
            time.sleep(7)
        elif self.__color_tl == 'красный':
            self.__color_tl = 'желтый'
            print(f'На светофоре {self.__color_tl} цвет.')
            time.sleep(2)
        elif self.__color_tl == 'желтый':
            self.__color_tl = 'зеленый'
            print(f'На светофоре {self.__color_tl} цвет.')
            time.sleep(7)


traff_light = TrafficLight()
while True:
    traff_light.running()
