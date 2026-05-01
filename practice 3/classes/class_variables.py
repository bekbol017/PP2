#1
class Car:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand

car1 = Car("Toyota")
car2 = Car("BMW")

print(car1.wheels)
print(car2.brand)


#2
class Student:
    school = "High School"

    def __init__(self, name):
        self.name = name

s1 = Student("Timur")
s2 = Student("Sanzhar")

print(s1.school)
print(s2.name)


#3
class Phone:
    company = "Apple"

    def __init__(self, model):
        self.model = model

p1 = Phone("iPhone 13")
p2 = Phone("iPhone 15")

print(p1.company)
print(p2.model)


#4
class Book:
    language = "English"

    def __init__(self, title):
        self.title = title

b1 = Book("Harry Potter")
b2 = Book("Dune")

print(b2.language)
print(b1.title)


#5
class Game:
    genre = "Action"

    def __init__(self, name):
        self.name = name

g1 = Game("Minecraft")
g2 = Game("GTA")

print(g1.genre)
print(g2.name)