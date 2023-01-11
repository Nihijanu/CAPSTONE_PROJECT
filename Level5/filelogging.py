import re
import logging

logging.basicConfig(filename="filelog2.txt", level=logging.INFO)
class searchLog():
    def _init_(self):
       pass
    def dearchLog(self,filename):
        file=open("filelog1.txt","r")
        str="ramya.txt"
        data=re.compile(str)
        res=data.search(str)
        line=file.readline()
        print(res.group(0))
# if _name=='main_':
#     obj=searchLog()
#     obj.dearchLog("ssssss1.txt")