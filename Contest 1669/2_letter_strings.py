for _ in range(int(input())):
    m = int(input())
    dc = {}
    for _ in range(m):
        s = input()
        dc[s] = dc.get(s, 0) + 1
    
    res = 0
    for k, v in dc.items():
        for c in range(ord('a'), ord('z') + 1):
            if chr(c) != k[0]:
                k2 = chr(c) + k[1]
                if dc.get(k2):
                    res += v * dc[k2]
            if chr(c) != k[1]:
                k2 = k[0] + chr(c)
                if dc.get(k2):
                    res += v * dc[k2]
    
    print(res // 2)