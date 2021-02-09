# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) # этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

class Clothe:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_coat(self):
        return self.size / 6.5 + 0.5

    def get_suit(self):
        return 2 * self.height + 0.3

    @property
    def get_full(self):
        return self.get_coat() + self.get_suit()


class Coat(Clothe):
    def __init__(self, size, height):
        super().__init__(size, height)

    def __str__(self):
        return str(self.get_coat())


class Suit(Clothe):
    def __init__(self, size, height):
        super().__init__(size, height)

    def __str__(self):
        return str(self.get_suit())


user_size = int(input('Введите размер:  '))
user_height = int(input('Введите рост:  '))

coat = Coat(user_size, user_height)
suit = Suit(user_size, user_height)

print(f'Расход ткани на пальто {coat} м.')
print(f'Расход ткани на костюм {suit} м.')
print(f'Всего общий подсчет расхода ткани составит {coat.get_full} метров.')
print(f'Сколько на пальто надо ткани? {coat.get_coat()} метров!')
print(f'Сколько на костюм надо ткани? {suit.get_suit()} метров!')
