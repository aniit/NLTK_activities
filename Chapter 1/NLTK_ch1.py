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
sent3[3]
[i for i, item in enumerate(sent3) if item == 'the']

#Activity 15
sorted (w for w in set(text5) if w.startswith('b'))

#Activity 16
list(range(10))
list(range(10,20))
list(range(10,20,2))
list(range(20,10,-2))

#Activity 17
text9.index('sunset')
text9[621:644]

#Activity 18
sent1
sorted(set([w for w in sent1+sent2+sent3+sent4+sent5+sent6+sent7+sent8 if w.isalpha()]))

#Activity 19
len(sorted(set(w.lower() for w in text1))) #len is lower here because the function turns firt tokens to lower case words and then order them, so repeated elements are delete
len(sorted(w.lower() for w in set(text1))) #len is higher here because the function orders words first, and after that, it turns tokens into lower case.

#Activity 20
print (not '!'.islower()) #it refers to any element which is not in lower case, incluing numbers and punctuation 
print ('!'.isupper()) 

#Activity 21
len(text2)
text2[141574:]

#Activity 22
freq = FreqDist([w for w in text5 if len(w) == 4])
w = len(freq)
list(reversed(freq.most_common(w)))

#Activity 23
len([item for item in text6 if item.isupper() and item.isalpha()])

#Activity 24
#ending in -ize
[a for a in text6 if a.endswith('ize')]
#containing -z-
[a for a in text6 if 'z' in a]
#Containing the sequence of letters pt
[a for a in text6 if 'pt' in a]
#Having all lowercase letters except for an initial capital (i.e., titlecase)
[a for a in text6 if a.istitle()]

#Activity 25
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
[i for i in sent if i.startswith('sh')]
[i for i in sent if len(i) > 4]

#Activity 26
lentok = sum(len(w) for w in text1) 
lentext = len(text1)
averlen = lentok/lentext #it is possible to work out the average word length of a text by diving sum(len(w) for in text) by len(text)
print(averlen) #in text 1, the average word length is 3.82

#Activity 27
def vocab_size(t):
    vocab = [word for word in t if word.isalpha()]
    return len(set(vocab))
vocab_size(text1)

#Activity 28
def percent(word,text):
    fw = FreqDist([word for word in text if word.isalpha()])
    return fw.freq(word) * 100
percent('I', text1)

#Activity 29
set(sent3) < set(text1) #it can be used to see whether a certain sentence is part of another text
