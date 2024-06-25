class Car:
    color = ""
    speed = 0

    def UpSpeed(self, val):
        self.speed += val

    def DownSpeed(self, val):
        self.speed -= val


## main
myCar1 = Car()
myCar1.color = "RED"
myCar1.speed = 0

myCar2 = Car()
myCar2.color = "BLUE"
myCar2.speed = 0

myCar3 = Car()
myCar3.color = "YELLOW"
myCar3.speed = 0

myCar1.UpSpeed(30)
print("Car1's color is %s and current speed is %dkm." % (myCar1.color, myCar1.speed))

myCar2.UpSpeed(60)
print("Car2's color is %s and current speed is %dkm." % (myCar2.color, myCar2.speed))

myCar3.UpSpeed(0)
print("Car3's color is %s and current speed is %dkm." % (myCar3.color, myCar3.speed))