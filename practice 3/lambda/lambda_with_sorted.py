students = [
    ("Aruzhan", 85),
    ("Dias", 92),
    ("Aigerim", 78)
]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


#2
students = [
    ("Nursultan", 85),
    ("Aidana", 92),
    ("Madi", 78)
]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)


#3
students = [
    ("Zhansaya", 85),
    ("Alibek", 92),
    ("Sanzhar", 78)
]
sorted_students = sorted(students, key=lambda x: x[0])
print(sorted_students)


#4
students = [
    ("Amina", 85),
    ("Bekzat", 92),
    ("Dana", 78)
]
sorted_students = sorted(students, key=lambda x: len(x[0]))
print(sorted_students)


#5
students = [
    ("Yerlan", 85),
    ("Madina", 92),
    ("Askar", 78)
]
sorted_students = sorted(students, key=lambda x: (x[1], x[0]))
print(sorted_students)