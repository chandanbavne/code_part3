#accept filename from user& display contents of that file

import os

file=input("Enter a file name :")

f=open(file,"r")
s=f.read()
print(s)
f.close()