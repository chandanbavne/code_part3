#2. Accept N numbers from user and return difference between frequency of
#even number and odd numbers.
#Input : N : 7
#Elements : 85 66 3 80 93 88 90
#Output : 1 (4 -3)

#required import module
from  array import *

def frq_diff(ls):
        even=0
        odd=0
        for i in ls:
            if(i%2)==0:
                even+=1
            else:
                odd+=1
        return(even-odd)




def main():             # define main function
    a=array('i',[])     # create empty array 
    n=int(input("enter a number of elements:"))
    for i in range(n):
        a.append(int(input("Enter a element:")))
    c=frq_diff(a)    
    print("difference between fruency of even& odd numbers:",c)




if __name__=="__main__":
    main()                  #main function call
