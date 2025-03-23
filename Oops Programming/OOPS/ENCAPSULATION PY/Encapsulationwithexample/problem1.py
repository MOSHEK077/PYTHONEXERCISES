class Student:
    def __init__(self):
        self.__grades = []  # Private attribute to store grades

    def add_grade(self, grade):
        """Adds a grade if it is between 0 and 100."""
        if 0 <= grade <= 100:
            self.__grades.append(grade)
            print(f"Grade {grade} added.")
        else:
            print(f"Invalid grade: {grade}. Must be between 0 and 100.")

    def calculate_average(self):
        """Returns the average of all grades or 0 if no grades are available."""
        if len(self.__grades) == 0:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def get_grades(self):
        """Returns a copy of the grades list to prevent direct modification."""
        return self.__grades.copy()

# Testing
s = Student()
s.add_grade(90)
s.add_grade(85)
s.add_grade(102)  # Invalid grade, should not be added
print("Grades:", s.get_grades())  # Output: [90, 85]
print("Average Grade:", s.calculate_average())  # Output: 87.5
