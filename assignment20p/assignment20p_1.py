#write a program which contains one clsss named as Bookstore.
#Bookstodr class containss two instance variabes as name,Author.
#that class contains one class variable as NoofBooks which is initialise to 0.
#there is one instance method of clas as Display() whcioh disopplays Name,Author,number of books.
#after creatinmg the class crete two objects of Bookstore class as
#obj1=Bookstore("Linux system programimng","Robert Love")
#obj1.display()
#obj2=Bookstore(" C programimng","Dennis Ritchie")

class Bookstore:    #create class
    NoOfBooks=0     #class variable
 #instance variable creation
    def __init__(self,n,a):
        self.name=n
        self.author=a
   #instance method
    def Display(self):
        Bookstore.NoOfBooks=Bookstore.NoOfBooks+1
        print(self.name,"by",self.author,'.',Bookstore.NoOfBooks)
 
#object creation:
obj1=Bookstore("Linux System Programming","Robert Love")
obj1.Display() 
print()

obj2=Bookstore("C Programming","Dennis Ritchie")
obj2.Display() 
