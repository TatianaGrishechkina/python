a = int(input('С какого результата спортсмен бегает? >>>'))
b = int(input('Какого результата ему надо достичь? >>>'))
i = 1
while a < b:
    print(f'День {i}, спортсмен пробежал {a} км из {b}')
    a = a + (a * 0.1)
    i += 1

print(f'День {i}, спортсмен пробежал {a} километров из {b}')
print(f'Спортсмен достигнет цели в {b} километров на {i} день!')