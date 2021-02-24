"""
You are given a 2D matrix, which represents the number of people in a room, grouped by 
their eye color and gender.
The first row represents the male gender, while the second row represents females.
The columns are the eye colors, in the following order: brown, blue, green, black

The data shows that, for example, there are 20 green eyed females in the room (2nd row, 3rd column).

Our program needs to take eye color as input and output the percentage of people 
with that eye color in the room. 
"""
# /brown /blue /green /black
data = [
  [23, 11, 5, 14], # males
  [8, 32, 20, 5]   # female
]
color = input()

total = 0

for i in range(len(data[0])):
  total = total + data[0][i]
  
for i in range(len(data[1])):
  total = total + data[1][i]


if color == 'brown':
  color_total = data[0][0] + data[1][0]

elif color == 'blue':
  color_total = data[0][1] + data[1][1]

elif color == 'green':
  color_total = data[0][2] + data[1][2]

elif color == 'black':
  color_total = data[0][3] + data[1][3]

percentage = color_total / total * 100
print(int(percentage))