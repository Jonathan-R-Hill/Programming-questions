'''
You're interviewing to join a security team. They want to see you build 
a password evaluator for your technical interview to validate the input.

Task: 
Write a program that takes in a string as input and evaluates it as a 
valid password. The password is valid if it has at a minimum 2 numbers, 
2 of the following special characters ('!', '@', '#', '$', '%', '&', '*'),
and a length of at least 7 characters.
If the password passes the check, output 'Strong', else output 'Weak'.

Input Format:
A string representing the password to evaluate.

Output Format:
A string that says 'Strong' if the input meets the 
requirements, or 'Weak', if not.
'''

# Password Validation

password = input()

a = ['!', '@', '#', '$', '%', '&', '*']

b = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

c = 0

d = 0

for i in range(len(password)):
    if password[i] in a:
        c = c + 1
        
    elif password[i] in b:
        d = d + 1
  
if c >= 2 and d >= 2 and len(password) >= 7:
    
    print('Strong')
    
else:
    
    print('Weak')