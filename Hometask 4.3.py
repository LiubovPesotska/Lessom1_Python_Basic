#Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.
#Ваше завдання - створити новий список з 3 елементів початкового списку - першим, третім і другим з кінця.

import random
numbers = []

# v1
numbers_len = random.randint(3, 10)
for _ in range(numbers_len):
    numbers.append(random.randint(3, 10))

print(numbers_len)
print(numbers)
