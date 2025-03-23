# Base class
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")

# Derived class (Hierarchical Inheritance)
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)  # Calls Person's __init__()
        self.student_id = student_id

    def show_student_info(self):
        print(f"Student ID: {self.student_id}")

# Another derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Calls Person's __init__()
        self.subject = subject

    def show_teacher_info(self):
        print(f"Subject: {self.subject}")

# Hybrid Inheritance - Teaching Assistant is both a Student and a Teacher
class TeachingAssistant(Student, Teacher):
    def __init__(self, name, student_id, subject):
        super().__init__(name, student_id)  # This will follow MRO
        self.subject = subject  # Manually set subject

    def show_ta_info(self):
        print(f"{self.name} is a Teaching Assistant, Student ID: {self.student_id}, Teaching: {self.subject}")

# Creating an object of TeachingAssistant
ta = TeachingAssistant("Alex", "S1234", "Physics")

# Calling methods
ta.show_name()           # From Person class
ta.show_student_info()   # From Student class
ta.show_teacher_info()   # From Teacher class
ta.show_ta_info()        # From TeachingAssistant class
