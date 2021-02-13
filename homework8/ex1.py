# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    user_date = ''

    def __init__(self, user_d):
        self.user_date = user_d

    @classmethod
    def split_date(cls, user_date):
        day, month, year = user_date.split('-')
        day = int(day)
        month = int(month)
        year = int(year)
        cls.validate(day, month, year)
        return day, month, year

    @staticmethod
    def validate(day, month, year):
        if not 1 <= month <= 12:
            print('Некорректный месяц!')
            return
        if month == 2:
            max_day = 29 if year % 4 == 0 else 28
        elif month in (1, 3, 5, 7, 8, 10, 12):
            max_day = 31
        else:
            max_day = 30
        if not 1 <= day <= max_day:
            print('Некорректный день!')
            return
        print('Дата корректна!')


user_data = input('Введите дату в виде строки "день-месяц-год":  ')
print(Date.split_date(user_data))

