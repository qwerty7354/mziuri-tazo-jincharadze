class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_info(self):
        print(f"{self.name} {self.surname}")


class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        self.students.pop(index)

    def show_students(self):
        for student in self.students:
            student.get_info()


my_school = School("Tbilisi School N1", "Tbilisi, Rustaveli Ave. 1")

student1 = Student("George", "Mamulashvili", 16)
student2 = Student("Mary", "Kvaratskhelia", 15)
student3 = Student("Luka", "Beridze", 17)

my_school.add_student(student1)
my_school.add_student(student2)
my_school.add_student(student3)

print("School students:")
my_school.show_students()