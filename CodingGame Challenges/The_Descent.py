import sys
import math

while True:

    max = 0
    tallest = 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        
        if mountain_h > max:
            max = mountain_h
            tallest = i

    print(tallest)