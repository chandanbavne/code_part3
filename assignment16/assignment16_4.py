#4. Accept N numbers from user and display all such elements which are
#divisible by 3 and 5.
#Input : N : 6
#Elements : 85 66 3 15 93 88
#Output : 15

# import required module:
from array import *

def div(ls):
    b=array('i',[])
    for i in ls:
        if(i%3==0 and i%5==0):
            b.append(i)
    return b        





def main():
    a=array('i',[])
    n=int(input("Enter a number of elements:"))
    for i in range(n):
        a.append(int(input("Arrays elements")))
    c=div(a)  # function call  
    for i in c:
        print("output:",i,end=" ")
    print()    


# code starter
if __name__=="__main__":
    main()