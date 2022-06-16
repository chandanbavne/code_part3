#3. Accept number of rows and number of columns from user and display below
#pattern.
#Input : iRow = 5 iCol = 5
#Output : $ * * * *
          # $ * * *
          # # $ * *
          # # # $ *
          # # # # $

row=int(input("Enter a number of rows:"))
col=int(input("Enter a number of column:"))
for i in range(0,row):
        for j in range(0,col):
            if(j<i):
                print("#",end=" ")
            elif(i==j):
                print("$",end=" ")
            else:
                print("*",end=" ")
        print()    
