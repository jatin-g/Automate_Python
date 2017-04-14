#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 20:36:04 2017

@author: Jatin
"""

import os, shutil

os.getcwd()
os.chdir('/Users/Shivam/Automate/Chapter 9/')


#This copies the file into heycopy folder with a new name
shutil.copy('OrganizeFiles.py','./heycopy/OrganizingFiles.py')

#This copies entire folder with it files into new folder anothercopyusingTree
shutil.copytree('heycopy','anothercopyusingTree')

#Note - shutil.copy does not copy folders

#Moving and Renaming
#Note if something with same name exist, it overwrites that
shutil.move('anothercopyusingTree','heycopy')


#Deleting the folders completely. 
shutil.rmtree('anothercopyusingTree')

#Another Safe way to delete is using Safe2trash module
import send2trash
newfile=open('bacon.txt','w')
newfile.write('bacon is something i cannot eat')
newfile.close()

#Send2trash sends file to recycle bin first
send2trash.send2trash('bacon.txt')

#os.walk to go through all subfolders and files within a folder
for foldername, subfolders, filenames in os.walk('heycopy'):
    print('The current folder is' + foldername)
    
    for subfolder in subfolders:
        print('SUBFOLDER OF' + foldername +':'+ subfolder)
        
        for filename in filenames:
            print('The File inside' + foldername + ': '+filename)
            
            
#Compressing files with zip module
#Reading contents of a zipfile
import zipfile, os
files=zipfile.ZipFile('Files.zip')
files.namelist()
spaminfo=files.getinfo('anothercopyusingTree/OrganizingFiles.py')
spaminfo.file_size
spaminfo.compress_size
print('Compressed file is %sX smaller' %(round(spaminfo.file_size/spaminfo.compress_size,2)))

#Extracting from ZIP Files
files=zipfile.ZipFile('Files.zip')
files.extractall()
files.close()
os.getwd()
