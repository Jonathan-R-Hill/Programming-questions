'''
You are a secret agent, and you receive an encrypted message 
that needs to be decoded. The code that is being used flips the message 
backwards and inserts non-alphabetic characters in the message to 
make it hard to decipher.

Task: 
Create a program that will take the encoded message, 
flip it around, remove any characters that are not a letter or a space, 
and output the hidden message.

Input Format:  
A string of characters that represent the encoded message.

Output Format: 
A string of character that represent the intended secret message.
'''

# The Spy Life Solution

import re

word = input()

b = word[::-1]
a = re.sub(r'[^A-Za-z ]', '', b)

print(a)