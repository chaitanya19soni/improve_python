class Vehical :
    def __init__ (self,brand , speed):
        self.brand = brand 
        self.speed = speed 
class Bike (Vehical):
    def __init__(self,brand , speed , gear):
        super().__init__(brand, speed)
        self.gear = gear
        print(f"{self.brand} with {self.speed} and {self.gear} number of gears ")

print("Name the brand")
name = input()
print("Tell us of what speed you want")
speed = int(input())
print("Tell us how many gears you want")
gear = int(input())


bk = Bike(name, speed ,gear)



    