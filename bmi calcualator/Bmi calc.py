import time
import logging


name = 'Jonathan Hill'
weight_kg = 98
height_m = 1.88


def calculate_bmi():

    bmi = round(weight_kg / (height_m ** 2), 2)

    print(name, 'your bmi is', bmi)


def weight_in_stone():
    weight_in_stone = round(weight_kg / 6.35, 2)
    print(name, 'your weight in stones is', weight_in_stone)


def height_in_feet():
    height_in_feet = round(height_m * 3.281, 2)
    print(name, 'your height in feet is', height_in_feet)


def weight_category():

    bmi = round(weight_kg / (height_m ** 2), 2)

    if bmi < 18.5:
        print(name, 'you are underweight')

    elif 18.5 <= bmi <= 24.99:
        print(name, 'you are at a healthy weight')

    elif 25.0 <= bmi <= 29.99:
        print(name, 'you are overweight')

    elif bmi > 30:
        print(name, 'you are obese')

calculate_bmi()
weight_in_stone()
height_in_feet()
weight_category()

print()

