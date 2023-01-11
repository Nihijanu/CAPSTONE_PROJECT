import logging
import os
logging.basicConfig(filename="stylelog1.txt",level=logging.WARNING)
class Filelog():
    def _init_(self):
        pass
    def find(self):
        try:
            f=open("sssss.txt","r")
        except FileNotFoundError as msg:
            logging.exception(msg)

if __name__=='__main__':
    obj=Filelog()
    obj.find()