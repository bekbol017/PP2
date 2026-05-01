#1
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def info(self):
        print(self.name, self.grade)

s = Student("Timur", "A")
s.info()


#2
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def info(self):
        print("Name:", self.name, "Grade:", self.grade)

s = Student("Timur", "B")
s.info()


#3
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_good(self):
        return self.grade == "A"

s = Student("Timur", "A")
print(s.is_good())


#4
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def change_grade(self, new_grade):
        self.grade = new_grade

s = Student("Timur", "C")
s.change_grade("A")
print(s.name, s.grade)


#5
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def info(self):
        print(self.name, self.grade)

s1 = Student("Timur", "A")
s2 = Student("Timur", "B")
s1.info()
s2.info()