#write a program which contains class name as Numbers.
#Arithmetic class contains one instance variables as value.
#inside init method initialise that instance variable to value which is accepted from user
#there are four instance methods inside class as chkprime(),chkperfect(),sumfactors(),factors()
#chkprime()method will returns True if number is prime otherwise return False.
#chkperfect()method will returns True if number is perfect ortherwise return False
#factors()method will display all factors of instance variable
#sumfactors()method will return addition of all factors use this merthod in any another method as helpert method if required
#create object


class Number:
    def __init__(self,v):       # INSTANCE VARIABLE
        self.number=v
    print()

#instance method
    def chkprime(self):
            for i in range(2,self.number):
                if(self.number%i)==1:
                    return True
                else:
                    return False
        
    def chkperfect(self):
            self.result=0
            for i in range(2,self.number):
                    if(self.number%i)==0:
                        self.result=self.result+i
            if (self.result==self.number):
                    return True
            else:
                    return False
            print()

    def factor(self):
            b=[]
            for i in range(2,self.number):
                if(self.number%i)==0:
                    b.append(i)
            for i in b:
                print(i,end=" ")
            print()
    def sumfactor(self):
            self.add=0   
            for i in range(2,self.number):
                if(self.number%i)==0:
                    self.add=self.add+i
            print("Addition of all factors is:",self.add)
            
obj1=Number(11)

ch=obj1.chkprime()            
print("result:",ch)
print()
obj2=Number(6)
d=obj2.chkperfect()
print("Result:",d)
print()
obj3=Number(12)
obj3.factor()
print()

obj4=Number(12)
obj4.sumfactor()            
                
                
                
            
            
        
                
                
    