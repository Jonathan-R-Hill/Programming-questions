import sys
import math

mylist = []

n = int(input()) # num of horses

for i in range(n):
    pi = int(input())
    mylist.append(pi) # strengths 

mylist.sort()

a = 100000

for i in range(len(mylist)): 

    if i + 1 < len(mylist):
        
        if mylist[i + 1] - mylist[i] < a:
            a = mylist[i + 1] - mylist[i]
            
print(a)