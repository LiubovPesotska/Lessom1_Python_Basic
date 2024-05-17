# Написати програму, яка переміщає всі нулі у кінець списку.
# Ваше завдання — змінити список так, щоб усі нулі опинилися наприкінці списку.
# Порядок ненульових чисел має зберегтися!
numbers = [1, 0, 2, 0, 4, 0, 1, 0, 6, 9]
new_numbers = []

for i in range(len(numbers)):
    if numbers[i] > 0:
        new_numbers.append(numbers[i])

print(new_numbers)

count_zeros = numbers.count(0)

print(count_zeros)

for _ in range(count_zeros):
    new_numbers.append(0)

print(numbers)
print(new_numbers)
