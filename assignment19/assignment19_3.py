#3)write a program which contains one calss named as Arithmetic.
#Inside init method initaialise all instance variable as value1,value1
#There are three instance method inside claas as Accept(), Addition(), SUbtraction(),
#Multiplication(),Division().
#Accept method will accept value of value1 and value2 from user.
#Addition method will perform addition of value1, value2 and return result.
#Subtraction methiod will perform subtraction of value1,value2 and return result.
#Multiplication() method will perform multiplication of value1,value2 and return result.
#Division() method will perform division of value1,value2 and return result.
#after desiginnig the above class call all instance metyhods by creating multiple objects.

class Arithmetic:               #class creation
    def __init__(self):         # constructor
    
        self.value1=0.0         # instance variable    
        self.value2=0.0         # instance variable    
        
    # instance method
    def Accept(self,m,n):
        self.value1=m
        self.value2=n
    print()
    
    def Addition(self):
        self.Add=self.value1+self.value2
        return self.Add
    print()
    
    def subtraction(self):
        self.sub=self.value1-self.value2
        return self.sub
    print()    
    
    def Multiplication(self):
        self.mult=self.value1*self.value2
        return self.mult
    print()
    
    def division(self):
        self.div=self.value1/self.value2
        return self.div
       
# object creaction

obj1= Arithmetic()
obj1.Accept(10,5)      
b=obj1.Addition()
print("Addtion of two  number is:",b)
print()
c=obj1.subtraction()
print("subtraction of two number is:",c)
print()
d=obj1.Multiplication()
print("Multipliction of two number is:",d)
print()
E=obj1.division()
print("Division of two number is:",E)