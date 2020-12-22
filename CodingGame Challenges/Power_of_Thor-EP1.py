import sys
import math

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]


lightx, lighty = light_x, light_y

intx, inty = initial_tx, initial_ty

while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move.

    DX = ""
    DY = ""

    if intx < lightx:
        DX = "E"
        intx += 1

    elif intx > lightx:
        DX = "W"
        intx -=1
        
    if inty < lighty:
        DY = "S"
        inty += 1

    elif inty > lighty:
        DY = "N"
        inty -= 1 

    print(DY + DX)
