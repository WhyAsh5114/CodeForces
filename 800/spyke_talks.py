n = int(input())
a = [int(x) for x in input().split()]

m = {}
for e in a:
    if e not in m and e != 0:
        m[e] = 1
    elif e != 0:
        m[e] += 1

pairs = 0
for e in m:
    if m[e] == 2:
        pairs += 1
    elif m[e] > 2:
        print(-1)
        break
else:
    print(pairs)