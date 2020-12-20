'''
You run a hovercraft factory. Your factory makes ten hovercrafts in a month.
Given the number of customers you got that month, did you make a profit? 
It costs you 2,000,000 to build a hovercraft, and you are selling them for 
3,000,000. You also pay 1,000,000 each month for insurance.

Task: 
Determine whether or not you made a profit based on how many of the ten hovercrafts 
you were able to sell that month.
 
Input Format: 
An integer that represents the sales that you made that month.

Output Format: 
A string that says 'Profit', 'Loss', or 'Broke Even'.
'''
# Hovercraft Solution

cost = 2000000
sellprice = 3000000
insurance = 1000000

amount_sold = int(input())

revenue = amount_sold * sellprice
costs = (cost * 10) + insurance

if revenue < costs:
    print('Loss')

elif revenue == costs:
    print('Broke Even')
    
elif revenue > costs:
    print('Profit')