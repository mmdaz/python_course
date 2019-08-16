class Pizza:
    def __init__(self, radius, toppings, slices=8):
        self.radius = radius
        self.toppings = toppings
        self.slices_left = slices

    def eat_slice(self):
        if self.slices_left > 0:
            self.slices_left -= 1

        else:
            print("Oh no! Out of pizza")

    @staticmethod
    def test_class_method():
        print("I am class method ")

    def __private_test_method(self):
        pass


if __name__ == '__main__':
    pizza_1 = Pizza(radius=30, toppings=["mashroom", "chicken"], slices=10)
    print(pizza_1.slices_left)
    pizza_1.eat_slice()
    print(pizza_1.slices_left)
    Pizza.test_class_method()
