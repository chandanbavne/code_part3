#2. Accept number of rows and number of columns from user and display below
#pattern.
#Input : iRow = 4 iCol = 4
#Output : * * * #
#         * * # @
#         * # @ @
#         # @ @ @

row=int(input("enter anumber of rows:"))
col=int(input("enter anumber of column:"))
for i in range(row,0,-1):
    for j in range(1,col+1):
        if(i==j):
            print("#",end=" ")
        elif(i>j):
            print("*",end=" ")
        else:
            print("@",end=" ")
    print()        

