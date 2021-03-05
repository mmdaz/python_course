class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def env(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return "width: {}, length: {}".format(self.width, self.length)


r1 = Rectangle(5, 7)
print(r1.area())
print(r1.env())

print(r1)

a = 1

print(a)
