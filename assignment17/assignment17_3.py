#3. Accept N numbers from user check whether that numbers contains 11 in
#it or not.
#Input : N : 6
#Elements : 85 66 11 80 93 88
#Output : 11 is present
#Input : N : 6
#Elements : 85 66 3 80 93 88
#Output : 11 is absent

#required import module
from array import *

def check(ls):              # check function definition
    for i in ls:
        if i in(11):
            print("11 is present")
        else:
            print("11 is absent")
            
def main():             # define main function
    a=array('i',[])     # create empty array 
    n=int(input("enter a number of elements:"))
    for i in range(n):
        a.append(int(input("Enter a element:")))
   
    check(a)# check function call    
    
if __name__=="__main__":    # code starter
    main()                  #main function call
