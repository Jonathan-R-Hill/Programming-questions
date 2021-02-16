"""
Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight.
 It’s calculated using a person's weight and height, using this formula: weight / height²

The resulting number indicates one of the following categories:
Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more

Let’s make finding out your BMI quicker and easier, by creating a program that 
takes a person's weight and height as input and outputs the corresponding BMI category.
"""

weight = float(input())
height = float(input())

bmi = weight / (height**2)

Underweight = bmi < 18.5
Normal = bmi > 18.5 and bmi < 25
Overweight = bmi > 25 and bmi < 30
Obesity = bmi > 30 

if Underweight:
    print('Underweight')

elif Normal:
    print('Normal')

elif Overweight:
    print('Overweight')

elif Obesity:
    print('Obesity')