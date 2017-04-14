#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 19:11:45 2017

@author: Jatin
"""
import os, shutil, re
#os.getcwd()
#os.chdir('/Users/Shivam/Automate/Chapter 9/ProjectDates')

#dateRegex=re.compile(r'''^(.*?)  - ^ is to check that pattern starts exactly as mentioned. .* is to match everything and ? is for zero or one
#((0|1)?\d)-                   - so month can be one or two digits so 0 or 1 with question mark means aero or one and \d means presence of a digit form 0-9
#((0|1|2|3)?\d)-            - so date could be starting from 0,1,2 or 3. in first digitso question mark and second digit will be \d
#((19|20)?\d\d)              - year will be starting with 19 or 20 or nothing so question mark and rest with 2 digits
#(.*?)$
#''',re.VERBOSE)

#First create a regex to extract american style dates MM-DD-YY

dateRegex=re.compile(r'''^(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)?\d\d)
(.*?)$
''',re.VERBOSE)

#os.listdir('.')
for amerfilename in os.listdir():
    mo=dateRegex.search(amerfilename)
    
    
    if mo==None:
        continue
    
    beforepart=mo.group(1)
    month=mo.group(2)
    day=mo.group(4)
    year=mo.group(6)
    afterpart=mo.group(8)
    
    euroFileName = beforepart + day +'-'+ month +'-'+ year + afterpart

    absWorkingDir = os.path.abspath('.')  #gives the abspath (fullpath)
    amerfilename = os.path.join(absWorkingDir,amerfilename)
    euroFileName = os.path.join(absWorkingDir,euroFileName)
    
    print('Renaming %s to %s' %(amerfilename,euroFileName))
    shutil.move(amerfilename,euroFileName)