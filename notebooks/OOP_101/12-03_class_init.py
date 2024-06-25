class Car:
    color = ""
    speed = 0

    def __init__(self):
        self.color = "RED"
        self.speed = 0

    def UpSpeed(self, val):
        self.speed += val

    def DownSpeed(self, val):
        self.speed -= val


## main
myCar1 = Car()
myCar2 = Car()

print("Car1's color is %s and current speed is %dkm." % (myCar1.color, myCar1.speed))
print("Car2's color is %s and current speed is %dkm." % (myCar2.color, myCar2.speed))