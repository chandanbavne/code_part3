#accept file name from user & display size of that file on screen.

import os

filename=input("Enter a file name: ")


print("size of file in bytes is {} ".format(os.path.getsize(filename)))