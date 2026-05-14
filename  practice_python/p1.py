class animal :
    def __init__(self, name ):
        self.name = name 
    def sound(self):
        print( self.name + "says bow")

class sent (animal):
    def ssente(self):
        print(f"{self.name}  is a good boy")

a = input()
b = sent (a)
b.sound()
b.ssente()