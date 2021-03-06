# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()),
# вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
# и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(),
# принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

class Cell:
    def __init__(self, nucleus):
        self.nucleus = int(nucleus)

    def __str__(self):
        return str(self.nucleus * "*")

    def __add__(self, other):
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):
        if self.nucleus - other.nucleus > 0:
            return Cell(self.nucleus - other.nucleus)
        else:
            raise ValueError

    def __mul__(self, other):
        return Cell(int(self.nucleus * other.nucleus))

    def __truediv__(self, other):
        return Cell(round(self.nucleus // other.nucleus))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.nucleus / cells_in_row)):
            row += f'{"*" * cells_in_row} \n'
        row += f'{"*" * (self.nucleus % cells_in_row)}'
        return row


# Объявляем ячейки
cells1 = Cell(12)
cells2 = Cell(3)
print(f'Как выглядит одна наша клетка: \n{cells1}')
print(f'Сложение двух клеток: \n{cells1 + cells2}')
print(f'Вычитание двух клеток: \n{cells1 - cells2}')
print(f'Умножение двух клеток: \n{cells1 * cells2}')
print(f'Деление двух клеток: \n{cells1 / cells2}')
try:
    print(cells2 - cells1)
except ValueError:
    print('Разность количества ячеек двух клеток меньше нуля!')

print(f'Пытаемся клетку разбить на ряды, где ряд больше количества ячеек: \n{cells2.make_order(12)}')
print(f'Пытаемся клетку разбить на ряды, где ряд больше количества ячеек: \n{cells1.make_order(3)}')
