# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

my_file = open('ex3.txt', encoding='utf-8')
min_salary = 20000

workers = my_file.readlines()
all_salary = 0

print('Зарплата больше 20000 у сотрудников:')

for worker in workers:
    name, salary = worker.split()
    salary = float(salary)
    if salary < min_salary:
        print(name)
    all_salary += salary


print(f"Средняя величина дохода у сотрудников: {all_salary / len(workers)}")

my_file.close()

