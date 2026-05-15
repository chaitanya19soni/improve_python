class Person :
    def __init__(self,name ):
        self.name =  name 

p = Person ('chaitnaya')
p.email = 'chaitnaya@1234'


print(hasattr(p, 'email'))