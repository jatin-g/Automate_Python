#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:34:05 2017

@author: Jatin
"""

Path='/Users/Shivam/Automate/Chapter 8 Files/File.py'

import os
os.path.join('usr','bin','spam')

#To get current working directory
os.getcwd()

#To change current working directory
#os.chdir('/Users/Shivam/Automate/Chapter 8 Files/')


#Giving a fixed path and different file in a list
myFiles=['work.txt','details.csv','invite.docx']
for file in myFiles:
    print(os.path.join('/Users/Shivam/Automate/Chapter 8 Files',file))
    
#Creating folders
#os.makedirs('/Users/Shivam/Automate/Chapter 8 Files/hey/')

#This gives the complete path of automate folder from the parent folder
print(os.path.abspath('./Automate'))

#Returns true or false if the path is absolute(full) or not
os.path.isabs('./hey/')
#
#os.path.relpath('/Users')

#Basename returns the file name and dirname returns the path
Path='/Users/Shivam/Automate/Chapter 8 Files/Files.py'
os.path.basename(Path)
os.path.dirname(Path)

#Using split we can have both base name and dirname in a tuple together
Filesplit=os.path.split(Path)
Filesplit()

os.path.getsize(Path)

os.listdir('//Users/Shivam/Automate/Chapter 8 Files')
 
#Program to get the total size of all files inside a folder chapter 8 files
totalsize = 0
for filename in os.listdir('//Users/Shivam/Automate/Chapter 8 Files/'):
    totalsize = totalsize + os.path.getsize(os.path.join('//Users/Shivam/Automate/Chapter 8 Files/',filename))  

print(totalsize)


print(os.path.getsize('//Users/Shivam/Automate/Chapter 8 Files/Files.py'))

#Check whether file exists or not. Returns true or False
os.path.exists('/Users/Shivam/Automate/Chapter 8 Files/')
os.path.exists('/Users/Shivam/Automate/Chapter 8 Files/anc.py')

#Reading and writing files. Create an open object first, then read from the object and print

#Reading
helloFile = open('/Users/Shivam/Automate/Chapter 8 Files/ReadFile.txt','r')
helloTxt= helloFile.read()
helloTxt

#Writing
WriteFile = open('/Users/Shivam/Automate/Chapter 8 Files/Write.txt','w')
WriteFile.write('Heyyy python')
WriteFile.close()
#Now reading from the Write.txt
WriteRead=open('/Users/Shivam/Automate/Chapter 8 Files/Write.txt','r')
Text=WriteRead.read()
Text

#Now Append
Veg=open('/Users/Shivam/Automate/Chapter 8 Files/Write.txt','a')
Veg.write('\nTomato is a vegetable')
Veg.close()

#Shelve
import shelve
shelfFile=shelve.open('mydata')
cats=['zophie','pooka','simon']
shelfFile['billi']=cats
shelfFile.close()

shelfFile= shelve.open('mydata')
shelfFile['billi']

type(shelfFile)
shelfFile.close()

#os.getcwd()
#os.chdir('/Users/Shivam/Automate/Chapter 8 Files/')

shelfFile = shelve.open('mydata')
list(shelfFile.keys())

list(shelfFile.values())
shelfFile.close()


#Pprint.pformat() - it returns the formatted representation of object as a string
#below it has saved a dictionary as a normal string in file mycats.py

import pprint
cats= [{'name':'gopu','desc':'slim'},{'name':'piku','desc':'fat'}]
pprint.pformat(cats)

fileobj=open('mycats.py','w')
fileobj.write('Cats = ' + pprint.pformat(cats) + '\n')
fileobj.close()

fileobj=open('mycats.py','r')
text=fileobj.read()
text

#when its saved in way above then the file is just a module that can be imported just like any other
import mycats
mycats.Cats
mycats.Cats[1]
