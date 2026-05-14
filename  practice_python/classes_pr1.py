class student :
    def __init__(self,name, marks):
        self.name = name 
        self.marks = marks
    def result(self):
        if (self.marks>=40):
            print(f"with {self.makrks} you are pass")
        else:
            print(f"with {self.marks} you are fail")

name =  input("Enter the name to find ")
marks = int(input("Enter marks to find the result"))

d = student(name , marks)
d.result()
