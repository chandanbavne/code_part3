#accept file name from user and create that file
import os

file=input("enter a file name:")
f=open(file,"a")
f.write("hello")

f.close()
