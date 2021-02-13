# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
class Warehouse:
    my_equipments = []

    def add_eq(self, equip):
        if not isinstance(equip, Equipment):
            raise ValueError('На складе может храниться только оборудование!')
        self.my_equipments.append(equip)

    def get_all_eq(self):
        return self.my_equipments


class Equipment:
    name: str
    price: float
    part_num: str


class Printer(Equipment):
    is_colour: bool


class Scanner(Equipment):
    paper_format: str


class Copier(Equipment):
    resolution: int
