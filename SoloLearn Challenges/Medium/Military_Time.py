'''
You want to convert the time from a 12 hour clock to a 24 hour clock. 
If you are given the time on a 12 hour clock, you should output the time 
as it would appear on a 24 hour clock.  

Task:  
Determine if the time you are given is AM or PM, 
then convert that value to the way that it would appear on a 24 hour clock.

Input Format: 
A string that includes the time, then a space and the 
indicator for AM or PM.

Output Format: 
A string that includes the time in a 24 hour format (XX:XX)
'''

# Military Time Solution

# This took me longer than any of the hard problems...

string = input()

time = string.split()

mylist = string.split(':')


  
if time[1] == 'PM':
    
    if int(mylist[0]) != 12:
        a = int(mylist[0]) + 12
        
        mylist[0] = str(a)
        mylist.insert(1, ':')
        
        c = ''.join(mylist)
        print(c[:5])

if time[1] == 'AM':
    
    if int(mylist[0]) == 12:
        mylist[0] = '00'
        mylist.insert(1, ':')
        c = ''.join(mylist)
        print(c[:5])
    
    elif int(mylist[0]) in range(10):
        mylist[0] = '0'+mylist[0]
        mylist.insert(1, ':')
        c = ''.join(mylist)
        print(c[:5])
    
    else:
        mylist.insert(1, ':')
        c = ''.join(mylist)
        print(c[:5])