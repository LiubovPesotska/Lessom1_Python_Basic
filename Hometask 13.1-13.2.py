#Hometask 13.1
# class Human:
#     def __init__(self, gender, age, first_name, last_name):
#         self.gender = gender
#         self.age = age
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}, {self.age} років, {self.gender}'
#
# class Student(Human):
#     def __init__(self, gender, age, first_name, last_name, record_book):
#         super().__init__(gender, age, first_name, last_name)
#         self.record_book = record_book
#
#     def __str__(self):
#         return f'{super().__str__()}, залікова книжка: {self.record_book}'
#
# class Group:
#     def __init__(self, number):
#         self.number = number
#         self.group = set()
#
#     def add_student(self, student):
#         self.group.add(student)
#
#     def delete_student(self, last_name):
#         student = self.find_student(last_name)
#         if student:
#             self.group.remove(student)
#
#     def find_student(self, last_name):
#         for student in self.group:
#             if student.last_name == last_name:
#                 return student
#         return None
#
#     def __str__(self):
#         all_students = '\n'.join(str(student) for student in self.group)
#         return f'Група номер {self.number}:\n{all_students}'
#
# # Приклади використання та тестування
# st1 = Student('Чоловік', 30, 'Стів', 'Джобс', 'AN142')
# st2 = Student('Жінка', 25, 'Ліза', 'Тейлор', 'AN145')
# gr = Group('PD1')
# gr.add_student(st1)
# gr.add_student(st2)
# print(gr)
#
# assert str(gr.find_student('Джобс')) == str(st1), 'Test1'
# assert gr.find_student('Джобс2') is None, 'Test2'
# assert isinstance(gr.find_student('Джобс'), Student) is True, 'Метод пошуку має повертати екземпляр'
#
# gr.delete_student('Тейлор')
# print(gr)  # Лише один студент
#
# gr.delete_student('Тейлор')  # Без помилки!
# Hometask 13.2

class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        if start < self.min_value or start > self.max_value:
            raise ValueError("Початкове значення повинно бути між мінімальним та максимальним значеннями")
        self.current = start

    def set_max(self, max_max):
        if max_max < self.min_value:
            raise ValueError("Максимальне значення не може бути менше мінімального значення")
        self.max_value = max_max

    def set_min(self, min_min):
        if min_min > self.max_value:
            raise ValueError("Мінімальне значення не може бути більше максимального значення")
        self.min_value = min_min

    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError("Досягнуто максимуму")
        self.current += 1

    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError("Досягнуто мінімуму")
        self.current -= 1

    def get_current(self):
        return self.current

# Приклади використання та перевірки
counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнуто максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Достигнуто мінімум
assert counter.get_current() == 7, 'Test4'
