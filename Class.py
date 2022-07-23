class Car:
    def __init__(self, brand, color, volume):
        self.brand = brand
        self.color = color
        self.volume = volume

    def drive_forvard(self):
        print("Drive forward")
    def drive_rewerse(self):
        print("Drive rewerse")

car = Car(brand="AUDI", color="Black", volume="2.4")
car.drive_forvard()
car.drive_rewerse()

print("-------------------------------")

class Car2(Car):

    @staticmethod
    def drive_left():
        print("Drive left")

    @staticmethod
    def drive_right():
        print("Drive right")

car = Car2(brand="VW", color="White", volume="1.6")
car.drive_forvard()
car.drive_rewerse()
car.drive_left()
car.drive_right()

print("------------------------------")

class Airplane:
    def __init__(self, model):
        self.airplane_model = model
    @staticmethod
    def up():
        print("Going up")

    @staticmethod
    def down():
        print("Going down")

#--------------------------------------

class FlyingCar(Car, Airplane):
    def __init__(self, brand, color, volume, model):
        Car2.__init__(self, brand, color, volume)
        Airplane.__init__(self, model)

flyingcar = FlyingCar(brand="VOLVO", color="Red", volume="2.0", model="S60")
flyingcar.up()
flyingcar.down()
flyingcar.drive_forvard()
flyingcar.drive_rewerse()