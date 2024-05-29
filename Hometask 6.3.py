# Ваше завдання — написати програму, яка перемножує всі цифри,
# введені користувачем цілого числа, поки воно не стане менше або дорівнювати 9.

number = int(input("Enter number: "))
print(number)

while number > 9:
    temp_number = str(number)
    number = 1
    for num in temp_number:
        number *= int(num)

    print(number)
