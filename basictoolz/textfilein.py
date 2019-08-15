#!/usr/bin/python3.7
#nanWarez
# inspired by: https://github.com/nanWarez/misc_etc/blob/master/filehandling.py
import time
from time import*

def textfilein():
 """function for textfile reading experimental state build v.0.0.2 [15.08.2019 12:50]"""

 lt = localtime()

 jahr, monat, tag = lt [0:3]
 print ("Datum: %02i.%02i.%04i" % (tag,monat,jahr))

 f = open("abc.txt", "r");
 print(f.readline(4))
 value = "Datum: %02i.%02i.%04i | achievement task produced for the day: \n" %(tag,monat,jahr)
 value2 = input("put into todays achievement -->here> ")
 value3 = "\n________________________________________________________________________\n"
 myString = str(value)
 myString2 = str(value2)
 myString3 = str(value3)
 myString4 = myString + myString2 + myString3
 #f.write(myString4)
 f.close()
#ab hier die score datei!
 scr = input("choose for todays score [a],[b],[c] type")
 if scr == 'a':
    scr = '100'
 elif scr == 'b':
    scr = '200'
 elif scr == 'c':
    scr = '500'
 else:
    print("you typed into a wrong input")

def search():
 """simple search function based on Line entries build v.0.0.1 [15.08.2019 22.13]""" 
 file = open("scr.txt", mode='r')
 cnt = 0
 found = 0
 search = input("enter prefered search word or entry: -->here> ")
 for printfile in file:
     cnt += 1
     printfile = file.readline(16)
     #print("testprint:!!!! ", printfile)
     if printfile == search:
        print("Entry found in Line:", cnt)
     else:
        #print("value not found")
 else:
     print("Entry hasnt been found!!!")

 file.close()


def testiter():
 """test iteration function for testing new things with this file v.000 [15.08.2019 22:14]""" 
 file = open("scr.txt", mode='r')
 cnt = 0
 search = input("enter prefered search word or entry: -->here> ")
 for printfile in file:
     cnt += 1
     printfile = file.readline(16)
     #print("testprint:!!!! ", printfile)
     if printfile == search:
        print("Entry found in Line:", cnt)
     #else: 
        #print("value not found")
 file.close()
