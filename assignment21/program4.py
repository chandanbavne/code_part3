# accept folder name from user and display all name of that file with its size
import os

folder=input("enter a folder name:")

for folder,subfolder,filename in os.walk(folder):
    for i in filename:
        print(f"file_name={i},sizeof file {os.path.getsize(i)}")
 

 #print("sizeof file",os.path.getsize(i))

