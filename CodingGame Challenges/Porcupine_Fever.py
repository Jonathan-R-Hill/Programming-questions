n = int(input())
y = int(input())

cages = []
total = 0

for i in range(n):
    s, h, a = [int(j) for j in input().split()] # Sick Healthy Alive
    cages.append([s, h, a])

for i in range(y):

    for i in range(len(cages)):

        if cages[i][0] > 0:
            new_sick = cages[i][0] * 2

            if new_sick > cages[i][1]:
                new_sick = cages[i][1]

            cages[i][1] -= new_sick
            cages[i][0] = new_sick

            total = total + cages[i][0] + cages[i][1]
        
        else:
            total = total + cages[i][0] + cages[i][1]

    if total <= 0:
        print("0")
        break
        
    print(total)
    total = 0   

