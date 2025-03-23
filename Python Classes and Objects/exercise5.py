class Classroom:
    def __init__(self, students=None):
        if students is None:
            students = []
        self.students = students

c1 = Classroom(["Alice", "Bob"])
