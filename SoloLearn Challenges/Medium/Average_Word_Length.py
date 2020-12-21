'''
You are in a college level English class, your professor wants you to write
an essay, but you need to find out the average length of all the words
you use. It is up to you to figure out how long each word
is and to average it out.

Task: 
Takes in a string, figure out the average length of all
the words and return a number representing the average length. 
Remove all punctuation. Round up to the nearest whole number.

Input Format: 
A string containing multiple words.

Output Format: 
A number representing the average length of each word, 
rounded up to the nearest whole number.
'''
# Average Word Length Solution

import math
import re


string = input()

string1 = re.sub('[^a-zA-Z0-9]+', ' ', string)

a =  string1.split()

total = 0

for i in range(len(a)):
    total = total + (len(a[i]))

if (total / len(a)) % 1 == 0:
    print(round(total / len(a)))
    
else:
    print(round(total / len(a) + .5))