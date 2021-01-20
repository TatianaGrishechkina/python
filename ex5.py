viruchka = int(input('Введите выручку >>> '))
izderzhki = int(input('Введите издержки >>>'))

if viruchka > izderzhki:
    pribil = viruchka - izderzhki
    print(f'Вы работаете с прибылью {pribil}')
    renta = pribil / viruchka
    print(f'Рентабельность = {renta}')
    sotrudniki = int(input('А сколько у вас сотрудников? >>>'))
    pribil_for_one = pribil / sotrudniki
    print(f'Один сотрудник зарабатывает для вас {pribil_for_one}!')
elif viruchka == izderzhki:
    print('Вы работаете в ноль! Остановитесь!!')
else:
    print(f'Вы работаете в убыток {viruchka - izderzhki}')
