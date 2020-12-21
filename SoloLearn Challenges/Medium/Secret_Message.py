'''
You are trying to send a secret message, and you've decided to encode 
it by replacing every letter in your message with its corresponding letter 
in a backwards version of the alphabet. 
What do your messages look like?

Task: 
Create a program that replaces each letter in a message with 
its corresponding letter in a backwards version of the English alphabet.

Input Format: 
A string of your message in its normal form.

Output Format: 
A string of your message once you have encoded it (all lower case).

'''

# Secret Message Solution

firstString = "abcdefghijklmnopqrstuvwxyz"

secondString = firstString[::-1]

string = input().lower()

translation = string.maketrans(firstString, secondString)

print(string.translate(translation))