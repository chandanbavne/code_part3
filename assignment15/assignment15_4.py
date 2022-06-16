#4. Accept number of rows and number of columns from user and display below
#pattern.
#Input : iRow = 6 iCol = 6
#Output : * * * * * *
#         * # # # * *
#         * # # * $ *
#         * # * $ $ *
#         * * $ $ $ *
#         * * * * * *


row=int(input("Enter a number of rows:"))
col=int(input("Enter a number of col:"))

for i in range(row,0,-1):
    for j in range(1,col+1):
        if(i==row or j==col or i==1 or j==1 or i==j):
            print("*",end=" ")
        elif(i>j and j>1):  
            print("#",end=" ")
        else:
            print("$",end=" ")
    print()        
        