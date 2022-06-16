#5. Accept number of rows and number of columns from user and display below
#pattern.
#Input : iRow = 4 iCol = 4
#Output : 1 2 3 4 5
#         1 2     5
#         1   3   5
#         1     4 5
#         1 2 3 4 5
row=int(input("Enter a number of rows:"))
col=int(input("Enter a number of column:"))

for i in range(1,row+1):
    for j in range(1,col+1):
        if(i==j or i==1 or i==row):
            print(j,end=" ")
        elif(j==1 or j==col):
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()        
