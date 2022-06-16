#1. Accept N numbers from user and return difference between summation
#of even elements and summation of odd elements.
#Input : N : 6
#Elements : 85 66 3 80 93 88
#Output : 53 (234 - 181)

# Required Imports(packages)
from math import *
from array import *

# Function to calculate sum of even number
def even(a):
    sum = 0
    for i in range(len(a)):
        if(a[i]%2)==0:
            sum = sum +a[i]
    return sum
    
# Function to calculate sum of odd number    
def odd(a):
    sum = 0
    for i in range(len(a)):
        if(a[i]%2)!=0:
            sum = sum +a[i]
    return sum
            
# Function to calculate difference of even and odd number
def diff(ls):
    even = 0
    odd = 0
    for i in (ls):
        if(i%2 == 0):
            even += i
        else:
            odd += i
    
    return (even-odd)


# main Function
def main():
    #Creating array
    a=array('i',[])
    n=int(input("Enter a number of arrays elements:"))
    for i in range(n):
        a.append(int(input("Enter a element:")))
    
    # calling even and odd function to get difference of Even and odd difference
    diff = (even(a)-odd(a))
    print("Difference of even and odd numbers:",diff)
# caling main function
main()