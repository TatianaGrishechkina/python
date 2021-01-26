time_in_sec = int(input('Введите время в секундах >>> '))
time_in_min = time_in_sec // 60
hours = time_in_min // 60
secs = time_in_sec % 60
mins = time_in_min % 60


print(f'{hours}:{mins}:{secs}')
