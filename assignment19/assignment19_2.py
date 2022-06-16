#2) write a program which contains one class named as Circle.
#Circle class contains three instance variables as Radius ,Area,Cicumferance.
#that class contains one class variable as PI which is initialise to 3.14
#inside init method initiaslise all instance variable to 0.0.
#There are three instance methods inside class as Accept(),ClaculateArea(),
#CalculateCircumference(),Display()
#Accept method() will aceppt value of Radius from user.
#CalculateArea() method will calculate Area of cicle and store it into instance variabvle area.
#CalculateCircumference() method will calcultae circumference of circle and store it into instance variable circumference.
#& Display ()method will display value of all the instance variable as Raius, area, circumference.
#After designing above class call all instance methods by creating multiple objects.

class Circle:
    PI=3.14 # class variable
#instance variables initializes in constructor
    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0
    #instance methods
    def Accept(self,r):
        self.Radius=r
    print()
    
    def Calculatearea(self,r):
        self.Area=(3.14*r**2)
        
    print()
    
    def CalculateCircumference(self,r):
        self.Circumference=2*3.14*r
        
    print()
    
    def Display(self):
           print("Radius of circle is:",self.Radius) 
           print("Area of circle is:",self.Area) 
           print("CIcumference of circle is:",self.Circumference) 
    print()

# object creataion
obj1=Circle()
obj1.Accept(10)
obj1.Calculatearea(10)
obj1.CalculateCircumference(10)

obj1.Display()    