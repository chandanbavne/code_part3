#4. Accept number of rows and number of columns from user and display below
#pattern.
#Input : iRow = 6 iCol = 6
#Output :

#: * * * *  *  *
#  * *         *
#  *   *       *
#  *     *     *
#  *        *  * 
#  * * *  * *  *
row=int(input("Enter a number of rows:"))
col=int(input("Enter a number of column:"))

for i in range(1,row+1):
    for j in range(1,col+1):
        if(i==1 or j==1 or i==row or j==col or i==j ):
            print("*",end=" ")
            
        else:
            print(" ",end=" ")
    print()        
            