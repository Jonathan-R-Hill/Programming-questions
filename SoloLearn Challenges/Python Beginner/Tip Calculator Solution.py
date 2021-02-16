"""
When you go out to eat, you always tip 20% of the bill amount. 
But who’s got the time to calculate the right tip amount every time? 
Not you that’s for sure! You’re making a program to calculate tips and save some time.

Your program needs to take the bill amount as input and output the tip as a float. 
"""

bill = int(input())

tip = bill / 100 * 20

print(tip)