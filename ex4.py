number = int(input('Введите положительное число >>> '))
max_num = 0

while number > 10:
    second_num = number % 10
    first_num = number // 10
    if second_num > max_num:
        max_num = second_num
    elif 10 > first_num > max_num:
        max_num = first_num
    number = number // 10
    print(max_num, first_num, second_num, number)

print(f'Наибольшая цифра - {max_num}')
