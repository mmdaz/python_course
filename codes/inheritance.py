class Animal:

    def __init__(self, type, name, speed=20):
        self.type = type
        self.name = name
        self.speed = speed

    def run(self):
        print("I am running ... speed :{}".format(self.speed))


class Fish(Animal):

    def __init__(self, color, name, type, speed):
        super().__init__(type, name, speed)
        self.color = color

    def swim(self):
        print("I am swimming ... speed : {}".format(self.speed))

    def run(self):
        print("I am a fish, I can't run !!!")


if __name__ == '__main__':
    fish = Fish(color="red", name="Nemo", type="x-larg", speed=30)
    fish.swim()
    fish.run()
