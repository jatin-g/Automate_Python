#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 02:19:49 2017

@author: Jatin
"""

#Pattern recognition type xxx-xxx-xxxx

def isPhonenumber(text):
        if len(text)!=12:
            
            return False
    
        for i in range(0,3):
            if not text[i].isdecimal():   #So here if isdecimal(means numeric) is False then not text[i] becomes true and returns false
                return False
                
        if text[3]!='-':
            return False
        
        for i in range(4,7):
            if not text[i].isdecimal():
                return False
                
        if text[7]!='-':
            return False
        
        for i in range(8,12):
            if not text[i].isdecimal():
                return False 
                
        return True



message='hey my number is 467-435-1245. call me me tomorrow or at office 435-123-3423'

for i in range(len(message)):
    chunk=message[i:i+12]
    if isPhonenumber(chunk):
        print("Phone Number found: ", chunk)
        
    

            
                