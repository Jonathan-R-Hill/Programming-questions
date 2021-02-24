"""
You are making a program to analyze text.
Take the text as the first input and a letter as the second input, 
and output the frequency of that letter in the text as a whole percentage.

Sample Input:
"""


text = input()
letter = input()


total = 0

for i in text:
    if i == letter:
        total += 1

answer = int(total / len(text) * 100)
print(answer)