# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    sorted_list = sorted([arg_1, arg_2, arg_3])
    return sorted_list[2] + sorted_list[1]


print(my_func(int(input('Введите первое число >> ')), int(input('Введите второе число >> ')), int(input('Введите '
                                                                                                        'третье число'
                                                                                                        ' >> '))))
