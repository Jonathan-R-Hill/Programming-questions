'''
You go trick or treating with a friend and all but three of the houses 
that you visit are giving out candy. One house that you visit is giving out 
toothbrushes and two houses are giving out dollar bills. 

Task
Given the input of the total number of houses that you visited, 
what is the percentage chance that one random item pulled from your bag is a dollar bill? 

Input Format 
An integer (>=3) representing the total number of houses that you visited. 

Output Format
A percentage value rounded up to the nearest whole number.
'''
# Halloween Candy Solution
import math

houses = int(input())

if houses >= 3:
    
    dollars = 200 / houses
    d = dollars  
    print(math.ceil(d))
    
else:
    print("You didn't visit enough houses")