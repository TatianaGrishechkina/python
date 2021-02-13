# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
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


xerox = Copier('Xerox')
sony = Printer('Sony')
toshiba = Printer('Toshiba')
lg = Scanner('LG')

warehouse = Warehouse()
for eq in [xerox, sony, toshiba, lg]:
    warehouse.add_eq(eq)

print(warehouse.get_all_eq_count())
warehouse.transf_eq_to_dept(toshiba, 'Accounting')
print(warehouse.get_all_eq_count())
