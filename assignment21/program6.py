#accept file name from user which is existing and accept one another file name
#create the newfile with the second name& copy the content of first file into second file

import os

file1=input("enter a file first from existing:")
file2=input("enter new file name:")

fr=open(file1,"r")
d=fr.read()
fw=open(file2,mode="w")
fw.write(d)
fr.close()
fw.close()