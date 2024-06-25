# 클래스 선언
class Car:
    speed = 0   # instance variable

    def upSpeed(self, val):
        self.speed += val

        print("current speed(super class): %d" % self.speed)

class Sedan(Car):
    def upSpeed(self, val):
        self.speed += val
        
        if self.speed > 150:
            self.speed = 150
        
        print ("current speed(sub class): %d" % self.speed)

class Truck(Car):
    pass

class Sonata(Sedan):
    pass

# 변수선언
sedan1, truck1, sonata1 = None, None, None

# main
truck1 = Truck()
sedan1 = Sedan()
sonata1 = Sonata()

print("Truck --> ", end = "")
truck1.upSpeed(200)

print("Sedan --> ", end = "")
sedan1.upSpeed(200)

print("Sonata --> ", end="")
sonata1.upSpeed(200)