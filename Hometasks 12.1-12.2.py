# Hometask 12.1
# import codecs
# import re
#
# def delete_html_tags(html_file, result_file='cleaned.txt'):
#     # Чтение HTML файла
#     with codecs.open(html_file, 'r', 'utf-8') as file:
#         html = file.read()
#
#     # Удаление HTML тегов с помощью регулярных выражений
#     clean_text = re.sub(r'<.*?>', '', html)
#
#     # Разделение текста на строки
#     lines = clean_text.splitlines()
#
#     # Удаление пустых строк и строк, содержащих только пробелы
#     meaningful_lines = [line.strip() for line in lines if line.strip()]
#
#     # Объединение строк обратно в один текст
#     cleaned_text = '\n'.join(meaningful_lines)
#
#     # Запись очищенного текста в выходной файл
#     with codecs.open(result_file, 'w', 'utf-8') as file:
#         file.write(cleaned_text)

#Hometask 12.2
class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f'{self.name}, ціна: {self.price}'

class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f'{self.name} {self.surname}'

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user

    def add_item(self, item, cnt):
        if item in self.products:
            self.products[item] += cnt
        else:
            self.products[item] = cnt

    def get_total(self):
        total = 0
        for item, cnt in self.products.items():
            total += item.price * cnt
        return total

    def __str__(self):
        items_str = '\n'.join([f'{item.name}: {cnt} pcs.' for item, cnt in self.products.items()])
        return f'User: {self.user}\nItems:\n{items_str}'

# Приклади використання
lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
print(lemon)  # lemon, ціна: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 30 pcs.
"""

assert cart.get_total() == 80, 'Повинно залишатися 80!'

print(cart.get_total())  # 80
