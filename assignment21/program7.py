#accept file name,create one string of 100 byte which  contains the name of that file &size #of that file
import os
file=input("enter a filename:")
size=os.pathgatesize(file)
filename=os.path.basename(file)
print(filename)
f=open(file)
header=(filename+" "+size)
n=len(header)
s
for i in range(n+1,101):
    header=header + " "
    