def calc_fs(s):
    fs = 0
    for i in range(len(s)-1):
        fs += s[i]*10 + s[i+1]
    return fs

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = [int(x) for x in list(input())]

    s.reverse()
    r1 = -1
    for i in range(n):
        if s[i] == 1:
            r1 = i
            break
    s.reverse()
    
    if r1 == -1:
        print(calc_fs(s))
        continue

    if r1 > 0 and k >= r1:
        s[n-1-r1], s[-1] = s[-1], s[n-1-r1]
        k -= r1
    
    l1 = -1
    for i in range(n-1):
        if s[i] == 1:
            l1 = i
            break
    
    if l1 > 0 and k >= l1:
        s[l1], s[0] = s[0], s[l1]

    print(calc_fs(s))