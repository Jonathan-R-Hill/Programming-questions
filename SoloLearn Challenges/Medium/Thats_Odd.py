'''
You want to take a list of numbers and find the sum of all of the 
even numbers in the list. Ignore any odd numbers.

Task:
Find the sum of all even integers in a list of numbers.

Input Format: 
The first input denotes the length of the list (N). 
The next N lines contain the list elements as integers.

Output Format: 
An integer that represents the sum of only the even numbers in the list.
'''

# That's odd.. Solution

length_of_list = int(input())

mylist = []

answer = 0

for num in range(length_of_list):
    
    a = int(input())
    mylist.append(a)


for i in range(len(mylist)):
    
    if mylist[i] % 2 == 0:
        answer = answer + mylist[i]
        
    else:
        continue

print(answer)