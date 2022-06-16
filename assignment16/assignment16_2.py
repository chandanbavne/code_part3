#2. Accept N numbers from user and display all such elements which are
#divisible by 5.
#Input : N : 6
#Elements : 85 66 3 80 93 88
#Output : 85 80
#required import module:
from array import * 

def division(a):        # define function
    b=array('i',[])
    for i in a:
        if (i%5)==0:
           b.append(i)
    return(b)       
           
       
             
                  



def main():
    n=int(input("Enter a number of elments:"))
    a=array('i',[])# empty array
    for i in range(n):
        a.append(int(input("Enter a elements:")))
    b=division(a) # function call
    for i in b:
        print(i,end=" ")
    print()    
        
if __name__=="__main__": # code starter
    main()