#5. Accept N numbers from user and display all such elements which are
#multiples of 11.
#Input : N : 6
#Elements : 85 66 3 55 93 88
#Output : 66 55 88

#import require module:
from array import *

def mult(ls):
    b=array('i',[])
    for i in ls:
        if(i%11)==0:
            b.append(i)
    return b        






# main Function
def main():
    #Creating array
    a=array('i',[])
    n=int(input("Enter a number of arrays elements:"))
    for i in range(n):
        a.append(int(input("Enter a element:")))
    # calling  mult function
    c=mult(a)
    for i in c:
        print(i,end=" ")
# caling main function
main()