def common_elements():
    # Генерация списка чисел кратных 3
    multiples_of_3 = {i for i in range(100) if i % 3 == 0}
    # Генерация списка чисел кратных 5
    multiples_of_5 = {i for i in range(100) if i % 5 == 0}

    # Нахождение пересечения множеств
    common_set = multiples_of_3 & multiples_of_5

    return common_set


# Примеры использования функции
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')