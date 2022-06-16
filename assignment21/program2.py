#accept directory name from user and display all filename from that folder on screen

import os

folder=input("Enter a directory name:")
ls=os.listdir(folder)
print(ls)