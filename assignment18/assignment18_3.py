#3. Accept N numbers from user and accept one another number as NO ,
#return index of last occurrence of that NO.
#Input : N : 6
#NO: 66
#Elements : 85 66 3 66 93 88
#Output : 3
#Input : N : 6
#NO: 93
#Elements : 85 66 3 66 93 88
#Output : 4
#Input : N : 6
#NO: 12
#Elements : 85 11 3 15 11 111
#Output : -1



#required module
from array import *
def check(ls,no):       # definine check function
    index=0
    for i in range(len(ls)):
        for j in ls:
            if(j==no):
                index+=1
    if(index<1):    
        return(-1)
    else:
        return(index)
        


def main():         # defin main function
    a=array('i',[]) #creating array
    n=int(input("Enter ano of elements:"))
    no=int(input("eneter a no for check"))
    for i in range(n):
        a.append(int(input("Enter a element:")))
    d=check(a,no)  # calling check function  
    print(d)


if __name__=="__main__":    # CODE STARTER
    main() #calling main function