"""
Given a string as input, use recursion to output each letter of the strings 
in reverse order, on a new line.

"""

def spell(txt):
    print(txt[::-1])
    

txt = input()
spell(txt)