#1. Accept N numbers from user and return frequency of even numbers.
#Input : N : 6
#Elements : 85 66 3 80 93 88
#Output : 3
#Required import module
from array import *
def Frq(ls):
    count=0
    for i in ls:
        if(i%2)==0:
            count+=1\
    return count        




def main():      #main function  definition
    # create array
    a=array('i',[])
    
    n=int(input("Number of elements of array"))
    for i in range(n):
        a.append(int(input("array element")))
    c=Frq(a)    # frequency function call to count the number of times elements arrived in array
    print("count of even numbers in array:",c)
        



#Code starter
if __name__=="__main__":
    main() #main function call