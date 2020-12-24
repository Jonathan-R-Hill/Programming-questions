import sys
import math
import numpy

n = int(input())  # the number of temperatures to analyse

temps = input().split()


Closest0 = sys.maxsize

if n <= 0:
    print(0)
    quit()
 

for i in range(n):

    T = int(temps[i])

    if abs(T) < abs(Closest0):
        
        Closest0 = T

    elif abs(T) == abs(Closest0):

        Closest0 = max(Closest0, T)

print(Closest0)