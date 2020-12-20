'''
You are cheering on your favorite team. After each play, 
if your team got over 10 yards further down the field, you stand up 
and give your friend a high five. If they don't move forward by at least a yard you stay quiet and say 'shh', 
and if they move forward 10 yards or less, you say 'Ra!' for every yard that they moved forward in that play.

Task 
Given the number of yards that your team moved forward,
output either 'High Five' (for over 10), 'shh' (for <1), 
or a string that has a 'Ra!' for every yard that they gained.

Input Format 
An integer value that represents the number of yards gained or lost by your team.

Output Format 
A string of the appropriate cheer. 
'''
# Cheer Creator Solution

a = int(input())

if a < 1:
    print('shh')

elif a <= 10 and a >= 1:
        print(a*'Ra!')
        
elif a > 10:
    print('High Five')
    
else:
    print('')