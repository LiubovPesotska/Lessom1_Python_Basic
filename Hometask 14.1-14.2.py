# #Hometask 14.1
# class GroupFullException(Exception):
#     """Exception raised when attempting to add more than 10 students to a group."""
#     def __init__(self, message="Cannot add more than 10 students to the group"):
#         self.message = message
#         super().__init__(self.message)
#
# class Group:
#     def __init__(self):
#         self.students = []
#
#     def add_student(self, student):
#         if len(self.students) >= 10:
#             raise GroupFullException()
#         self.students.append(student)
#
#     def __str__(self):
#         return f"Group with {len(self.students)} students."
#
# def main():
#     group = Group()
#     try:
#         for i in range(11):  # Attempt to add 11 students
#             group.add_student(f"Student {i+1}")
#             print(f"Added Student {i+1}")
#     except GroupFullException as e:
#         print(f"Exception: {e}")
#
# if __name__ == "__main__":
#     main()
# Hometask 14.2
class GroupFullException(Exception):
    """Exception raised when attempting to add more than 10 students to a group."""
    def __init__(self, message="Cannot add more than 10 students to the group"):
        self.message = message
        super().__init__(self.message)

class Student:
    def __init__(self, gender, age, first_name, last_name, student_id):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self):
        return hash(str(self))

class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise GroupFullException()
        self.students.append(student)

    def delete_student(self, last_name):
        self.students = [student for student in self.students if student.last_name != last_name]

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        return f"Group {self.name} with {len(self.students)} students."

def main():
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    gr = Group('PD1')
    gr.add_student(st1)
    gr.add_student(st2)
    print(gr)
    assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
    assert gr.find_student('Jobs2') is None

    gr.delete_student('Taylor')
    print(gr)  # Only one student

if __name__ == "__main__":
    main()
