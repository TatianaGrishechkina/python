# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
from collections import Counter


class Warehouse:
    my_equipments = []
    my_counter = Counter()

    def add_eq(self, equip):
        if not isinstance(equip, Equipment):
            raise ValueError('На складе может храниться только оборудование!')
        self.my_equipments.append(equip)
        self.my_counter.update((type(equip).__name__,))

    def transf_eq_to_dept(self, equip, dept):
        if equip not in self.my_equipments:
            raise ValueError('На складе нет такого оборудования!')
        self.my_equipments.remove(equip)
        self.my_counter.subtract((type(equip).__name__,))
        print(f'{equip} передано в подразделение {dept}')

    def get_all_eq(self):
        return self.my_equipments

    def get_all_eq_count(self):
        return dict(self.my_counter)


class Equipment:
    name: str
    price: float
    part_num: str

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Printer(Equipment):
    is_colour: bool


class Scanner(Equipment):
    paper_format: str


class Copier(Equipment):
    resolution: int


class NumberException(Exception):
    def __init__(self, txt):
        self.txt = txt


warehouse = Warehouse()
while True:
    inp_data = input("Введите 1 чтобы добавить оборудование, 2 чтобы перевести оборудование в отдел или 0 для выхода: ")
    if inp_data == '0':
         break
    elif inp_data == '1':
        eq_name = input("Введите название оборудования: ")
        inp_type = input("Введите тип оборудования, 1 - принтер, 2 - сканер, 3 - ксерокс:  ")
        if inp_type == '1':
            warehouse.add_eq(Printer(eq_name))
        elif inp_type == '2':
            warehouse.add_eq(Scanner(eq_name))
        elif inp_type == '3':
            warehouse.add_eq(Copier(eq_name))
        else:
            print('Несуществующий тип оборудования!')
    elif inp_data == '2':
        eqs = warehouse.get_all_eq()
        for i, eq in enumerate(eqs):
            print(f'{i}={eq}')
        num_eq = input('Введите порядковый номер оборудования для передачи:  ')
        dep = input('Введите отдел, куда необходимо перевести оборудование:  ')
        warehouse.transf_eq_to_dept(eqs[i], dep)
    else:
        print('Неверная операция!')
    print(f'Оборудование на складе: {warehouse.get_all_eq_count()}')

