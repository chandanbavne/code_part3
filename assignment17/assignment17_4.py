#4. Accept N numbers from user and return frequency of 11 form it.
#Input : N : 6
#Elements : 85 66 3 15 93 88
#Output : 0
#Input : N : 6
#Elements : 85 11 3 15 11 111
#Output : 2

# required module
from array import *

def frq(ls):             #define frq function
    count=0
    for i in ls:
        if(i==11):
            count=count+1
    return count        


def main():             # define main function
    a=array('i',[])     # create empty array 
    n=int(input("enter a number of elements:"))
    for i in range(n):
        a.append(int(input("Enter a element:")))
    c=frq(a)    # calling frq function
    print("frequency is:",c)




if __name__=="__main__":
    main()                  #main function call
