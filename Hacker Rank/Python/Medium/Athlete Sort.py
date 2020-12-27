import math
import os
import random
import re
import sys


nm = input().split()
n = int(nm[0])
m = int(nm[1])

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
    
k = int(input())

a = (sorted(arr, key=lambda data: data[k]))

for i in a:
    b = (str(i).strip('[],'))
    c = re.sub(r'[^A-Za-z0-9 ]', '', b)
    print(c)