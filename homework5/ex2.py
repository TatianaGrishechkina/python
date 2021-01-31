# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_file = open('ex2.txt')
lines = [line for line in my_file.readlines()]

print(f'В файле {len(lines)} строк')

for el in lines:
    el1 = el.replace('\n', '')
    print(f"В строке {el1} -- {len(el.split())} слов")

my_file.close()
