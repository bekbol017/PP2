import os
with open("sample.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("Python is awesome\n")
    f.write("File handling\n")
    f.write("W3Schools\n")
    f.write("Practice 06\n")

#1
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

#2
with open("sample.txt", "r") as f:
    line = f.readline()
    while line:
        print(line, end="")
        line = f.readline()

#3
with open("sample.txt", "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines, 1):
        print(f"[{i}] {line.strip()}")

#4
try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())
except FileNotFoundError as e:
    print(f"Error: {e}")

#5
with open("sample.txt", "r") as f:
    print(f.read(30))