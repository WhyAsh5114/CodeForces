from math import ceil

for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    
    m = {}
    for e in a:
        if e not in m:
            m[e] = 1
        else:
            m[e] += 1
    
    dbl = 0
    sgl = 0
    for e in m:
        if m[e] >= 2:
            dbl += 1
        else:
            sgl += 1
    
    print(dbl + ceil(sgl / 2))
