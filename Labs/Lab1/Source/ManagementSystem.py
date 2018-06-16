class Person:
    def __init__(self):
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.gender = input("Gender: ")

    # Method to display student Data
    def display(self):
        print("\nName: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)


class Marks:
    def __init__(self):
        self.stuClass = input("Class: ")
        print("Enter the marks of the respective subjects")
        self.math = int(input("Math: "))
        self.chemistry = int(input("Chemistry: "))
        self.physics = int(input("Physics: "))

    # Method to display Student and Marks details
    def display(self):
        print("Study in: ", self.stuClass)
        print("Total Marks: ", self.math + self.chemistry + self.physics)


class GradeSystem:
    def __init__(self, passorfail):
        self.passorfail = passorfail

    # Method to display student Data
    def display(self):
        print("\nStudent (P/F): ", self.passorfail)


# Multiple Inheritance
class Student(Person, Marks):
    def __init__(self):
        # Super Call
        super(Student, self).__init__()
        # Calling Constructors
        Person.__init__(self)
        Marks.__init__(self)

    def result(self):
        # Call Methods to display details
        Person.display(self)
        # Call method of class 'marks'
        Marks.display(self)


# Created Instances of class
stu1 = Student()
stu2 = Student()

# Call method of class Student
stu1.result()
stu2.result()