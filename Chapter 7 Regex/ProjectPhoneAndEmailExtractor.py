#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 23:26:03 2017

@author: Jatin
"""
#Pyperclip to copy and past string. Regex for PhoneNumber and email.


#phoneRegex=re.compile(r'''(
#(\d{3}|\(\d{3}\))?                 #this is to handle brackets-(  \d{3} | \(  \d{3} \)   )? 
#(\s|-|\.)?                         # \s this is space |-| \. this is for dot
#\d{3}
#(\s|-|\.)?
#\d{4}
#(\s*(ext|x|ext.)\s*\d{2,5})?
#)''',re.VERBOSE | re.I)

import pyperclip, re
matches=[]

phoneRegex=re.compile(r'''(
(\d{3}|\(\d{3}\))?                
(\s|-|\.)?
(\d{3})
(\s|-|\.)?
(\d{4})
(\s*(ext|x|ext.)\s*\d{2,5})?
)''',re.VERBOSE | re.I)


emailRegex=re.compile(r'''(
[a-zA-Z0-9._%+-]+
\@
[a-zA-Z0-9._%+-]+
(\.[a-zA-Z]{2,4})

)''',re.VERBOSE)

text=str(pyperclip.paste())

for groups in phoneRegex.findall(text):
    phoneNum='-'.join([groups[1],groups[3],groups[5]])
    if groups[6]!='':
        phoneNum += ' x' + groups[6]
    matches.append(phoneNum)

    for groups in emailRegex.findall(text):
        matches.append(groups[0])
        
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to Clipboard")
    print('\n'.join(matches))
    
else:
    print("No phone number or email address found")

        

#
#Email=emailRegex.findall("ajsbas email isdsd jatin1230@gmail.com jatingarg@email.co")
#
#
#mo=phoneRegex.search(text)
#pyperclip.copy(mo)
#print(mo.group())




