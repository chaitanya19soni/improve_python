class Book :
    def __init__(self,title,author ,page):
        self.title = title 
        self.author = author
        self.page = page
    def __str__(self):
        return f"{self.title} by {self.author} - {self.page} pages"
    
print ("What is the title")
Title = input ()
print ("Who is the author")
Author =  input()
print("On what page number")
Page =  int (input ())

kitab = Book(Title,Author,Page)
print(kitab)