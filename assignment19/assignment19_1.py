#1) write a program which contaims one class named as Demo
#Demo class contains two instance variables as no1,no2.
#that class contains one class variable as value.
#there are two instance methods as Fun and Gun which displays values of instance variables
#initialise instance variable in init method by accepting the values from user.

# After creating the class create the two objects pf Demo clas as
#Obj1=Demo(11,21) 
#Obj2=Demo(51,101)

#now call the instance methods as
#obj1.Fun()
#obj2.Fun()
#obj1.Gun()
#obj2.Gun()

class Demo:
    value='m'
    
  #constructor
    def __init__(self,m,n):
        self.no1=m
        self.no2=n
   #instance method
    def Fun(self):
            print("value of instance variable is:",self.no1)
            print("value of instance variable is:",self.no2)
    
    def Gun(self):
            print("value of instance variable is:",self.no1)
            print("value of instance variable is:",self.no2)
        
obj1=Demo(11,21)        
obj2=Demo(51,101)

obj1.Fun()        
obj2.Fun()        
obj1.Gun()        
obj2.Gun()        
    
 