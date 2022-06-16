#5. Accept number of rows and number of columns from user and display below
#pattern.
#Input : iRow = 4 iCol = 4
#Output : 1 2 3 4
#           2 3 4
#             3 4
#               4

row=int(input("Enter a number of rows:"))
col=int(input("Enter a number of column:"))
for i in range(0,row):
    for j in range(1,col+1):
        if(j>i):
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()        