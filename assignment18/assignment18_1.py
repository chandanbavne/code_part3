#1. Accept N numbers from user and accept one another number as NO ,
#check whether NO is present or not.
#Input : N : 6
#NO: 66
#Elements : 85 66 3 66 93 88
#Output : TRUE
#Input : N : 6
#NO: 12
#Elements : 85 11 3 15 11 111
#Output : FALSE


#required module:
from array import *
def check(ls,no):   # defining check function
    count=0
    for i in ls:
        if(i==no):
            count+=1
    if (count>1):
        return True
    else:
        return False
   
    
    


def main():         # defin main function
    a=array('i',[]) #creating array
    n=int(input("Enter ano of elements:"))
    no=int(input("eneter a no for check"))
    for i in range(n):
        a.append(int(input("Enter a element:")))
    d=check(a,no)  # calling check function  
    print(d,)


if __name__=="__main__":    # CODE STARTER
    main() #calling main function