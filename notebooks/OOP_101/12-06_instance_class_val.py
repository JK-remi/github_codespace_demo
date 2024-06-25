# 클래스 선언
class Car:
    color = ""  # instance variable
    speed = 0   # instance variable
    count = 0   # class variable

    def __init__(self):
        self.speed = 0
        Car.count += 1

# 변수선언
myCar1, myCar2 = None, None

# main
myCar1=Car()
myCar1.speed = 30
print("Car1's current speed is %dkm, %d cars are created." % (myCar1.speed, Car.count))

myCar2=Car()
myCar2.speed = 60
print("Car2's current speed is %dkm, %d cars are created." % (myCar2.speed, myCar2.count))