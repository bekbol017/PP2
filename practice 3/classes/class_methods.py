#1
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

c = Calculator()
print(c.add(3, 4))
print(c.multiply(3, 4))


#2
class Calculator:
    def subtract(self, a, b):
        return a - b

    def divide(self, a, b):
        return a / b

c = Calculator()
print(c.subtract(10, 3))
print(c.divide(10, 2))


#3
class Calculator:
    def power(self, a, b):
        return a ** b

    def mod(self, a, b):
        return a % b

c = Calculator()
print(c.power(2, 5))
print(c.mod(17, 5))


#4
class Calculator:
    def max_num(self, a, b):
        return max(a, b)

    def min_num(self, a, b):
        return min(a, b)

c = Calculator()
print(c.max_num(8, 12))
print(c.min_num(8, 12))


#5
class Calculator:
    def area_rect(self, w, h):
        return w * h

    def perim_rect(self, w, h):
        return 2 * (w + h)

c = Calculator()
print(c.area_rect(5, 3))
print(c.perim_rect(5, 3))