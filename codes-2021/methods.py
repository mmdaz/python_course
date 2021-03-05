class MyClass:
    y = 10

    def __init__(self, x):
        self.x = x

    def instance_method(self):
        return 'instance method called', self

    @classmethod
    def class_method(cls):
        return 'class method called', cls

    @staticmethod
    def static_method():
        return 'static method called'


c1 = MyClass(4)
c2 = MyClass(5)
print("c1.x: ", c1.x)
print("c2.x: ", c2.x)

print("c1.y: ", c1.y)
print("c2.y: ", c2.y)

c1.x = 8

print("c1.x: ", c1.x)
print("c2.x: ", c2.x)

c1.y = 15

print("c1.y: ", c1.y)
print("c2.y: ", c2.y)

MyClass.y = 15

print("c1.y: ", c1.y)
print("c2.y: ", c2.y)
