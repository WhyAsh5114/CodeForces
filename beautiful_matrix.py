a = []
for y in range(5):
    a.append([int(x) for x in input().split()])

for y in range(5):
    for x in range(5):
        if a[y][x] == 1:
            print(abs(y-2) + abs(x-2))