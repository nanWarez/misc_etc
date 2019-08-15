#!/usr/bin/python3.7
#nanWarez
#inspired by: https://github.com/nanWarez/misc_etc/blob/master/filehandling.py
import time
from time import*

def textfileout():

 lt = localtime()

 jahr, monat, tag = lt [0:3]
 print ("Datum: %02i.%02i.%04i" % (tag,monat,jahr))

 f = open("achievements.txt", "a");
 print (f)
 value = "Datum: %02i.%02i.%04i | achievement task produced for the day: \n" %(tag,monat,jahr)
 value2 = input("put into todays achievement -->here> ")
 value3 = "\n----------------------------------------------------------------------------------------------------\n"
 myString = str(value)
 myString2 = str(value2)
 myString3 = str(value3)
 myString4 = myString + myString2 + myString3
 f.write(myString4)
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
 print('You scored %s.' %scr)
 file = open("scr.txt", mode='a')
 file.write('Printed string %s.\n' %scr)
 file.close()

def score(scr):
 print('score(valueireceived) func here You scored %s.' %scr)
 file = open("scr.txt", mode='a')
 file.write('Printed string: %s.\n' %scr)
 value2 = input("put into todays achievement -->here> ")
 value3 = "\n----------------------------------------------------------------------------------------------------\n"
 myString2 = str(value2)
 myString3 = str(value3)
 myString4 = myString2 + myString3
 file.write(myString4)
 file.close()



def readme():

 lt = localtime()
 print(lt)
 jahr, monat, tag, stunde, minute = lt [0:5]
 print ("[%02i.%02i.%04i %02i:%02i]" % (tag,monat,jahr,stunde,minute))

 f = open("Readme.md", "a");
 print (f)
 value = "[%02i.%02i.%04i %02i:%02i] | achievement task produced for the day: \n" %(tag,monat,jahr,stunde,minute)
 value2 = input("put into todays achievement -->here> ")
 value3 = "\n----------------------------------------------------------------------------------------------------\n"
 myString = str(value)
 myString2 = str(value2)
 myString3 = str(value3)
 myString4 = myString + myString2 + myString3
 f.write(myString4)
 f.close()

def timestamp():

 lt = localtime()
 print(lt)
 jahr, monat, tag, stunde, minute = lt [0:5]
 #print ("[%02i.%02i.%04i %02i:%02i]" % (tag,monat,jahr,stunde,minute))
 f = open("scr.txt", 'a');
 print(f)
 value = "[%02i.%02i.%04i %02i:%02i]\n" %(tag,monat,jahr,stunde,minute)
 myString4 = str(value)
 f.write(myString4)
 f.close()

