"""
Given a sentence as input, calculate and output the average word length of that sentence.
To calculate the average word length, you need to divide the sum of all word lengths by 
the number of words in the sentence. 
"""
text = input()

a = text.split(' ')

total = 0

for i in a:
    total = total + len(i)

print(total / len(a))