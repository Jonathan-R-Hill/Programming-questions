'''
You have to get a new driver's license and you show up at the office
at the same time as 4 other people. The office says that they will see
everyone in alphabetical order and it takes 20 minutes for them to process
each new license. All of the agents are available now, and they can each
see one customer at a time. How long will it take for you to walk out
of the office with your new license?

Task 
Given everyone's name that showed up at the same time, 
determine how long it will take to get your new license.

Input Format 
Your input will be a string of your name, then an integer 
of the number of available agents, and lastly a string of the other
four names separated by spaces.

Output Format 
You will output an integer of the number of minutes that it will
take to get your license.
'''
# New Drivers License Solution 

name = input().lower()
agents = int(input())
que = input().lower().split()

que.append(name)

a = sorted(que)

pos = a.index(name)

if agents == 1:
    print((pos + 1) * 20)

else:
    print(int(pos // agents) * 20 + 20)
