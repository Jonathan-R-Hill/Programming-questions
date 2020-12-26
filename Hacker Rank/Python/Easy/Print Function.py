if __name__ == '__main__':
    n = int(input())

a = []

for i in range(n):
    a.append(i+1)

b = ''.join([str(x) for x in a])
print(b)