'''
You and your friends are going to Europe! You have made plans to travel 
around Europe with your friends, but one thing you need to take into 
account so that everything goes according to play, is that the format 
of their date is different than from what is used in the United States. 
Your job is to convert all your dates from MM/DD/YYYY to DD/MM/YYYY.

Task: 
Create a function that takes in a string containing a date 
that is in US format, and return a string of the same date converted to EU.

Input Format: 
A string that contains a date formatting 11/19/2019 or November 19, 2019.

Output Format: 
A string of the same date but in a different format: 19/11/2019.
'''
# Convert US Date to EU Date Solution
import re

date = input()

d = {
"January":"1",
"February":"2",
"March":"3",
"April":"4",
"May":"5",
"June":"6",
"July":"7",
"August":"8",
"September":"9",
"October":"10",
"November":"11",
"December":"12"
    
}

if len(date) <= 10:
    
    short = date.split('/')
    
    x = short[1]
    y = short[0]
    z = short[2]
    print(f'{x}/{y}/{z}')
    
else:
    ld = re.sub(r'[^A-Za-z0-9] ', ' ', date)
    a = ld.split()
    
    a = ' '.join(str(d.get(word, word)) for word in a)
    b = a.split()
    
    x = b[1]
    y = b[0]
    z = b[2]
    
    print(f'{x}/{y}/{z}')