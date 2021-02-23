"""
Given a string as input, you need to output how many times each letter appears in the string.
You decide to store the data in a dictionary, with the letters as the keys, 
and the corresponding counts as the values.
Create a program to take a string as input and output a dictionary, which represents the letter count. 
"""

text = input()

count = {} 
  
for i in text: 

    if i in count: 
        count[i] += 1

    else: 
        count[i] = 1

print(count)