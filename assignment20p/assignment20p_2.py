#write a program which contains one class named as BankAccount
#that class contains one class variable as ROI which is initialise to 10.5.
#BankAccount class contains two instance variables as Name and Amount
#Inside init method initialise all name and amount variables by accepting the values from user
#there are four instance methods inside class as Display(),Deposit(),Withdraw(),CalculateIntrest()
#Deposit()method will accept the amount from user and add that value in class instance variable amount
#withdraw() method will accept amount to be withdrawn from user and subtract that amount from class variable amount
#CalculateIntrest()method calculate the instrest based on amount by considering rate of intrest which is class variable as ROI
#Display()methdo will display value of all variable as Name and Amount
#create object

class BankAccount:   #class create
    ROI=10.5      #class variable
    def __init__(self,n,am):    # constructor/instance variables
        self.name=n
        self.Amount=am
        
    # instance methods:
    def Deposit(self,a):
        self.Amount=a
        print("class instance variable amount is:",self.Amount)
    print()
        
    def withdraw(self,wa):
        self.withdrawamount=wa
        self.remain=(self.Amount - self.withdrawamount)
        print("remaining amount in account is:",self.remain)
    print()
    
    def CalculateIntrest(self):
        self.intrest=self.Amount*BankAccount.ROI
        print(self.intrest)
    def display(self):
        print("instance variable is:",self.name)
        print("instance variable is:",self.Amount)
        
obj1=BankAccount("SBI",15000)
obj1.Deposit(20000)
obj1.withdraw(12000)
obj1.CalculateIntrest()
obj1.display()        