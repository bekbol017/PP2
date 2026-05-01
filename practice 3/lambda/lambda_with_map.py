#1
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))
print(squares)


#2
numbers = [1, 2, 3, 4]
doubles = list(map(lambda x: x * 2, numbers))
print(doubles)


#3
numbers = [1, 2, 3, 4]
plus_one = list(map(lambda x: x + 1, numbers))
print(plus_one)


#4
words = ["hi", "python", "Bekbol"]
lengths = list(map(lambda w: len(w), words))
print(lengths)


#5
names = ["bekbol", "almaty", "python"]
upper_names = list(map(lambda s: s.upper(), names))
print(upper_names)