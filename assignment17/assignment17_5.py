#5. Accept N numbers from user and accept one another number as NO ,
#return frequency of NO form it.
#Input : N : 6
#NO: 66
#Elements : 85 66 3 66 93 88
#Output : 2
#Input : N : 6
#NO: 12
#Elements : 85 11 3 15 11 111
#Output : 0

# required module
from array import *
def frq(ls,no):
    
    count=0
    for i in ls:
        if(i==no):
            count=count+1
    return count        




def main():             # define main function
    a=array('i',[])     # create empty array 
    n=int(input("enter a number of elements:"))
    no=int(input("enter a number to check exact matching number:"))

    for i in range(n):
        a.append(int(input("Enter a element:")))
    
    c=frq(a,no)    # frq calling function
    print("count the frquency of exact number:",c)




if __name__=="__main__":
    main()                  #main function call
