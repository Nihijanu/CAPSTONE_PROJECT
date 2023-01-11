import os
def find(filename,path):
    for root,dir,files in os.walk(path):
        for name in files:
            if name==filename:
                print("file exist")
                break
        else:
            print("not found")
            break
name=input("fiename")
dir=input("dir:")
find(name,dir)