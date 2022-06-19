for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]

    m = {}
    for e in a:
        m[e] = m.get(e, 0) + 1
    
    ans, evens = 0, 0
    for e in m:
        if m[e] % 2 == 1:
            ans += 1
        else:
            evens += 1
    ans += evens - (evens % 2)
    
    print(ans)
