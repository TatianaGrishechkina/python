# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
# и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b} * i'

    def __add__(self, other):
        return ComplexNum(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNum(self.a * other.a - self.b * other.b, self.a * other.b + other.a * self.b)


num1 = ComplexNum(1, 2)
num2 = ComplexNum(3, 4)

print(f'Первое комплексное число: z = {num1}')
print(f'Второе комплексное число: z = {num2}')
print(f'Сумма двух комплексных чисел: z = {num1 + num2}')
print(f'Произведение двух комплексных чисел: z = {num1 * num2}')

