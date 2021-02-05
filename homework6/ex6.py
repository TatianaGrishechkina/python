# 6. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self):
        super().__init__('ручка')

    def draw(self):
        super().draw()
        print(f'{self.title} пишет синим.')


class Pencil(Stationery):
    def __init__(self):
        super().__init__('карандаш')

    def draw(self):
        super().draw()
        print(f'{self.title} пишет серым.')


class Handle(Stationery):
    def __init__(self):
        super().__init__('маркер')

    def draw(self):
        super().draw()
        print(f'{self.title} пишет красным.')

uno = Pen()
blue = Pencil()
tres = Handle()

for unit in {uno, blue, tres}:
    unit.draw()
