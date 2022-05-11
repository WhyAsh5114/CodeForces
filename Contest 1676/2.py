t = int(input())

a = []
for i in range(t):
    l = input()
    a.append([int(x) for x in input().split()])

for case in a:
    m = min(case)
    to_eat = 0
    for box in case:
        to_eat += box - m
    print(to_eat)
