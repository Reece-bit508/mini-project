# Class definition for Student
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.__grade = grade  # private attribute (encapsulation)

    # Getter method for grade
    def get_grade(self):
        return self.__grade

    # Setter method for grade
    def set_grade(self, grade):
        self.__grade = grade

    # Method to display student info
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.__grade}")

# Subclass inheriting from Student
class GraduateStudent(Student):
    def __init__(self, name, age, grade, degree):
        super().__init__(name, age, grade)
        self.degree = degree

    # Method overriding (polymorphism)
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.get_grade()}")
        print(f"Degree: {self.degree}")

# Create at least 3 student objects
student1 = Student("Alice", 20, "A")
student2 = Student("Bob", 22, "B+")
grad_student = GraduateStudent("Charlie", 25, "A", "MSc Computer Science")

# Print their details
print("---- Student 1 ----")
student1.display_info()
print("\n---- Student 2 ----")
student2.display_info()
print("\n---- Graduate Student ----")
grad_student.display_info()