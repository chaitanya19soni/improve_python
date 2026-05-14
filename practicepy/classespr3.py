class Car :
    def __init__ (self , brand , speed):
        self . brand = brand
        self.speed = speed
    
    def accelerate(self,amount):
        self.speed = self.speed +amount 
        print (f" {self.speed} the increased acceleration")
       
    

print("what brand and amount to change acceleration ")
automobile = input("Enter your fav brand")
speed = int (input("What is the current speed")) 
amount =  int (input("How much to accelerate "))
d =  Car (automobile,speed)
d.accelerate(amount)
