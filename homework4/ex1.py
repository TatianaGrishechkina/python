# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def salary(work_time, per_hour, bonus):
    return work_time * per_hour + bonus


try:
    file, work_time_arg, per_hour_arg, bonus_arg = argv
except ValueError:
    print('Invalid args')
    exit()

print(salary(int(work_time_arg), int(per_hour_arg), int(bonus_arg)))
