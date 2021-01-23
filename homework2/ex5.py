# 5. Реализовать структуру «Рейтинг», представляющую собой
# не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]

# print(f'Наш список {my_list} {max_num}') # предварительный список
i = 'y'

while i == 'y':
    custom_num = int(input('Введите любое число >>> '))
    max_num = max(my_list)
    if custom_num > max_num:
        my_list.insert(0, custom_num)
    elif custom_num in my_list:
        my_list.insert(-my_list[::-1].index(custom_num), custom_num)
    else:
        my_list.append(custom_num)
    print(f'Наш Рейтинг {my_list}')
    i = input('Хотите ввести еще одно число? (y/n) >>> ').lower()
