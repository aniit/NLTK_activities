# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 19:55:19 2017

@author: Cristina
"""

#NLTK_Chapter 1
from nltk.book import *
text1
text2

#Activity 1
2+2

#Activity  2
26 ** 10
26 ** 100

#Activity 3
['Monty', 'Python'] * 20
3 * sent1

#Activity 4
len(text2) #tokens
len(set(text2)) #types

#Activity 5
def lexical_diversity():
    return len(set(text) / len(text))
    
#humor (0.231) is more diverse than fiction:romance (0.121)

#Activity 6
text2.dispersion_plot(['Elinor', 'Marianne', 'Edward', 'Willoughby'])

#Females are the main characters of the novel. Elinor and Edward/ Marianne and Willobough as it is represented by the dispersion plot

#Activity 7
text5.collocations()

#Activity 8
len(set(text4))
#to know about the types in text 4

#Activity 9
#a
var1 = 'One apple a day keeps the doctor away'
var1
print(var1)

#b
var1 * 2
var1 + '.'

#Activity 10
idiom = ['One', 'apple', 'a', 'day', 'keeps', 'the', 'doctor', 'away']
print(idiom)
''.join(idiom)
' '.join(idiom)
'One apples  day keeps the doctor away'.split()

#Activity 11
w1 = ['One']
w2 = ['apple']
w3 = ['a']
w4 = ['day']
w5 = ['keeps']
w6 = ['the']
w7 = ['doctor']
w8 = ['away']

idi = w1+w2+w3+w4+w5+w6+w7+w8
print(idi)
idi
len(w1 + w2)
len(w1) + len(w2)

#Activity 12
'Monty Python'[6:12] #characterers 
['Monty','Python'][1] #words

#Activity 13
sent1[2][2] #object in position 2 in superobject with position 2
sent1 #Call me Ishmael

#Activity 14
sent3
x = 'the'
while x in sent3:
    print(sent3.index(x))
