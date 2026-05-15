class Animal:
    def __init__(self,name):
        self.name = name 
    def speak(self):
        return"..."
class Dog (Animal):
    def speak(self):
        return "WOOF"
class Cat (Animal):
    def speak (self):
        return "MEOW"

feline = input("Enter cat name:")
dogesh =  input ("Enter the dog name:")

neko = Cat (feline)
eenu = Dog (dogesh)

print(f"{eenu.name} says {eenu.speak()}")
print(f"{neko.name} says {neko.speak()}")