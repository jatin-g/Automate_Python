#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:49:25 2017

@author: Jatin
"""
import os, random
os.getcwd()
#os.chdir('/Users/Shivam/Automate/Chapter 8 Files/ProjectQuiz/')

capitals= {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
   
  
#Generate 35 quiz files
# %s is a placeholder which replaces its values from quizNum+1

for quizNum in range(35):
    quizFile = open('capitalQuiz %s' % (quizNum+1), 'w')
    answerKeyFile = open('capitalQuiz_Answers %s' %(quizNum+1), 'w')
    #Header for quizfiles
    
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '*20) + 'State Capitals Quiz (Form %s)' % (quizNum+1))
    quizFile.write('\n\n')
    
    states=list(capitals.keys())
    random.shuffle(states)
    
    #Now looping through all 50 states and making a question for each
    
    for questionNum in range(50):
        #Get right and worng answers
        #Below step will store all capitals corresponding to all states in correctAnswer
        #it will be something like states[0] to states[49]
        correctAnswer=capitals[states[questionNum]]
        
wrongAnswer = list(capitals.values())
        #Now delete right answer from wrong answer list
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer=random.sample(wrongAnswer,3)
        answerOptions =  wrongAnswer + [correctAnswer]
        random.shuffle(answerOptions)
        
        
        #write question and answer now
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum+1,states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' %('ABCD'[i], answerOptions[i] ))
        quizFile.write('\n')
        
        #write anser keys to a file
        answerKeyFile.write('%s %s\n' %(questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))
        
    quizFile.close()
    answerKeyFile.close()
            
            
            
        
    
    
    
    
    
    