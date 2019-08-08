class CarFactory:
    speed = 120

    def __init__(self, color, bogh_sound):
        self.color = color
        self.bogh_sound = bogh_sound

    def drive(self):
        print("I am driving ... sepeed : {}".format(self.speed))

    def bogh(self):
        print(self.bogh_sound)


if __name__ == '__main__':

    # car_1 = CarFactory(color="red", bogh_sound="Boooooog")
    # car_2 = CarFactory(color="blue", bogh_sound="Heeeeeeeeey")
    # car_1.color = "green"
    # car_1.bogh()
    # car_2.bogh()
    car_1 = CarFactory()
    car_1.drive()
