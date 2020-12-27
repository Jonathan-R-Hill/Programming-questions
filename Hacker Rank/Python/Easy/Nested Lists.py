mylist = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mylist.append([score, name])

mylist.sort()


b = [i for i in mylist if i[0] != mylist[0][0]]
c = [j for j in b if j[0] == b[0][0]]

for i in range(len(c)):
    print(c[i][1])
