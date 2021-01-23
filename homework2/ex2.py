#2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

#list_original = ['Адъ', 42, 0.5, None, 777, 'L', -1, 6, 0]

original = input('Введите слово >> ')

list_original = list(original)
count = len(list_original)
print(f'Количество элементов в списке: {count}')

list_reverse = list()
i = 1
j = None

while i <= count:
    list_reverse.extend(list_original[i:j:-1])
    j = i
    i += 2

print(f'Начальный список: {list_original}.')
print(f'Список с обменом соседних элементов: {list_reverse}.')


