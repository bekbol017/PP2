#1
with open("output.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")
print("File created: output.txt")

#2
with open("output.txt", "a") as f:
    f.write("Third line (appended)\n")
    f.write("Fourth line (appended)\n")
with open("output.txt", "r") as f:
    print(f.read())

#3
try:
    with open("new_file.txt", "x") as f:
        f.write("Created with mode x\n")
    print("new_file.txt created!")
except FileExistsError:
    print("File already exists!")

#4
students = ["Alice\n", "Bob\n", "Charlie\n", "Diana\n", "Eve\n"]
with open("students.txt", "w") as f:
    f.writelines(students)
with open("students.txt", "r") as f:
    print(f.read())

#5
data = [
    ("Alice", 90),
    ("Bob", 85),
    ("Charlie", 92),
]
with open("grades.txt", "w") as f:
    f.write("Name,Grade\n")
    for name, grade in data:
        f.write(f"{name},{grade}\n")
with open("grades.txt", "r") as f:
    print(f.read())