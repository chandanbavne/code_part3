#3. Accept N numbers from user and display all such elements which are
#even and divisible by 5.
#Input : N : 6
#Elements : 85 66 3 80 93 88
#Output : 80

# import array module
from array import *

def even_div(a):
    b=array('i',[])
    for i in a:
        if(i%2)==0:
            if(i%5)==0:
                b.append(i)
    return b        





def main():
    n=int(input("Enter a number of elments:"))
    a=array('i',[])# empty array
    for i in range(n):
        a.append(int(input("Enter a elements:")))
    b=even_div(a) # function call
    for i in b:
        print(i,end=" ")
    print()    
        
if __name__=="__main__": # code starter
    main()