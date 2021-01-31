# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_file = open("ex4.txt", encoding='utf-8')
new_file = open("ex4_new.txt", "w", encoding='utf-8')
rus_num = ['Один', 'Два', 'Три', 'Четыре']

lines = my_file.readlines()
only_num = [int(line[-2]) for line in lines if line != '\n']
list_with_rus = "\n".join(f'{rus_num[n - 1]} - {n}' for n in only_num)

print(list_with_rus)
new_file.write(list_with_rus)

my_file.close()
new_file.close()
