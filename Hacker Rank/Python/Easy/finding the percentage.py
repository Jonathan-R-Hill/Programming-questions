n = int(input())
marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    marks[name] = scores
query_name = input()

total = 0
count = 0

for key, values in marks.items():
    for i in values:
        if query_name == key:
            total += i
            count += 1
            
a = total / count

print(f'{a:.2f}')