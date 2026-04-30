#1
numbers = [1, 2, 3, 4, 5]
for x in numbers:
  print(x)
  if x == 3:
    break

#2
for x in "python":
  print(x)
  if x == "t":
    break

#3
for i in range(1, 10):
  if i == 6:
    break
  print(i)

#4
numbers = [10, 20, 30, 40]
for x in numbers:
  if x == 30:
    break
  print(x)

#5
for i in range(1, 100):
  print(i)
  if i == 10:
    break