#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 00:26:17 2017

@author: Jatin
"""

#Program to add bullets and text to the text



import pyperclip
text= pyperclip.paste()       #pyperclip.paste() brings the copied text from clipboard to text


lines = text.split('\n')      #text.split will split the copied text as per each line which is done by \n#if we dont put \n then it will split by each and put > in each space
for i in range(len(lines)):
    lines[i]='> ' + lines[i]
    
text='\n'.join(lines)         #with text='\n'.join(lines) we join all the different lines 
pyperclip.copy(text)          #because pyperclip.copy is expecting a single string not list of string values
            




