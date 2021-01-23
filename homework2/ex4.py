# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

custom_text = input('Введите строку из нескольких слов >>> ')

list_text = list(custom_text.split())

len_text = len(list_text)
i = 0

while i < len_text:
    if len(list_text[i]) < 10:
        print(f'{i + 1}. {list_text[i]}')
        i += 1
    else:
        short_word = list_text[i]
        print(f'{i + 1}. {short_word[0:10]}')
        i += 1

