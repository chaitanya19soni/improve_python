class Circle:
    pi =3.14
    def __init__(self, r):
        self. r = r

    def area(self):
       return Circle.pi * self.r**2

    def perimeter(self):
        return  2 * Circle.pi * self.r

    def result(self):
        print(f"The area is {self.area()} and the perimeter is {self.perimeter():.4f} ")



print("type the radius ")
r = int (input())
geo = Circle(r)
geo.result()