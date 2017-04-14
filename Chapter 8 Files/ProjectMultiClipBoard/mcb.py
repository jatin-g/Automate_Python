#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:28:50 2017

@author: Jatin
"""

import shelve, pyperclip, sys

#os.getcwd()
#os.chdir('/Users/Shivam/Automate/Chapter 8 Files/ProjectMultiClipBoard/')



#len(sys.argv)
#print('hey')
#print(sys.argv)
mcbShelf = shelve.open('mcb')
#print(mcbShelf)
#print(len(sys.argv))
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    
    mcbShelf[sys.argv[2]]= pyperclip.paste()
    print('Saved')
elif len(sys.argv)==2:
    if sys.argv[1].lower() == 'list':
#        print('2 list')
#        print(str(list(mcbShelf.keys())))
        pyperclip.copy(str(list(mcbShelf.keys())))
        
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        
        
mcbShelf.close()