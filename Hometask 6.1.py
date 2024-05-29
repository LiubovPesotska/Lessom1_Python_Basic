 #Користувач вводить через дефіс дві літери, Ваше завдання написати програму,
# яка повертатиме всі символи між ними включно.
#
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
#
# Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв


import string

letters = string.ascii_letters

user_text = input("Enter letters in format 'a-c' ").strip()

if len(user_text) == 3 and user_text[0].isalpha() and user_text[1] == "-" and user_text[2].isalpha():
    first_letter = user_text[0]
    second_letter = user_text[2]

    start_index = ord(first_letter)
    end_index = ord(second_letter) + 1

    if start_index > end_index:
        start_index, end_index = end_index, start_index

    for symbol_number in range(start_index, end_index):
        current_symbol = chr(symbol_number)
        if current_symbol.isalpha():
            print(current_symbol, end="")