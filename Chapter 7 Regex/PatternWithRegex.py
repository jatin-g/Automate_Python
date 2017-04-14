#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 02:53:54 2017

@author: Jatin
"""
#regexpal to get regular expressions
import re  #all regex functions in python are in re module so importing

def phonenumber(text):
    phoneNumberRegex= re.compile(r'(\d{3})-(\d{3}-\d{4})')
    mo=phoneNumberRegex.search(text)
    
    print("Number found", mo.group()) #mo has pattern calling group() on mo to return the match
    print(mo.groups())                 #we have made two groups above with brackets so returning groups
    print(mo.group(2))
    areacode, mainnumber=mo.groups()  #first group goes to area code and second to mainnumber
    print(areacode)
    print(mainnumber)
    
    
message="hey my number is 467-435-1245. call me me tomorrow or at office 435-123-3423"
phonenumber(message)



# Now we will use pipe | operator to look for multiple groups...or condition

def regpattern(mess):
    MultiReg=re.compile(r'Jatin|GARG|garg|Garg|\d{3}-\d{3}-\{4}')
    mo=MultiReg.search(mess)
    print("found", mo.group())
    
message1="my name is Jatin GARG garg and number is 469-655-1706"
regpattern(message1)


#(wo)? below is optional ? checks for occurence
batregex = re.compile(r'Bat(wo)?man')
mo1=batregex.search('The Batman adventures')
print(mo1.group())

#(wo)* checks for multiple or NONE occurence of pattern
batregex1=re.compile(r'Bat(wo)*man')
mo2=batregex1.search('The Batwowowowowowoman is awesome')
print(mo2.group())

#(wo)+ checks for ONE OR MORE occurence of pattern
batregex1=re.compile(r'Bat(wo)+man')
mo2=batregex1.search('The Batwowowowowowoman is awesome')
print(mo2.group())

#Greedy and Non Greedy. Greedy matches longest instance while NonGreedy matches shortest instance

greedyregex=re.compile(r'(ha){3,5}')      #GreedyExample 
mo1=greedyregex.search("hahahahahahah")
print(mo1.group())

nonGreedyReg=re.compile(r'(ha){3,5}?')    #NonGreedy example with a Question Mark
mo2=nonGreedyReg.search("hahahaha")
print(mo2.group())

#Findall function to find all instances
findInst=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  #NO GROUPS HERE
mo=findInst.findall('the number is 469-655-1706 and other is 263-567-1345')
print(mo)                                    #This returns list

findInst=re.compile(r'(\d{3})-(\d{3}-\d{4})')  
mo=findInst.findall('the number is 469-655-1706 and other is 263-567-1345')
print(mo)                                   #This returns tuple as there are groups


#Making own character class 
vowelregex=re.compile(r'[aeiouAEIOU]')      #This searches for all these characters
mo=vowelregex.findall("we are the best we are thw wineers")
print(mo)

consonant=re.compile(r'[^aeiouAEIOU]')      #This searches for all characters which are not these
mo=consonant.findall("we are the best we are thw wineers")
print(mo)


#Wildcard character. dot character
wildRegex=re.compile(r'ca.')               #This matches just one character as per dot
mo=wildRegex.findall("california moca poca soca roca") #if it were .ca then oca oca will be result
print(mo)

#Matching everything with dot star

wildRegex=re.compile(r'.*ca')               #This matches just one character as per dot
mo=wildRegex.findall("california mocaas pocaas soca roca jhjj jhf") #if it were .ca then oca oca will be result
print(mo)

#To ignore case sensitive, add re.I or re.Ignorecase as an argument. Below will work with small B too
batregex1=re.compile(r'Bat(wo)+man', re.IGNORECASE)
mo2=batregex1.search('The batwowowowowowoman is awesome')
print(mo2.group())

#Sub method, here replcaing word before Agent with censored. PLACEMENT of \w \s MATTERS
namesRegex=re.compile(r'\w+ Agent\s', re.I)
mo=namesRegex.sub('Censored','raj Agent is great and shivam agent too')
print(mo)

