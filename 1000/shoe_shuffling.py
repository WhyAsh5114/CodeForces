for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    m = {}
    for e in a:
        if e in m:
            m[e] += 1
        else:
            m[e] = 1

    valid = True
    for k in m:
        if m[k] < 2:
            valid = False
            print("-1")
            break
    
    if not valid:
        continue

    pos = 1
    p = []
    for k, v in m.items():
        tp = list(range(pos, pos+v))
        last = tp[-1]
        tp.pop(len(tp) - 1)
        tp.insert(0, last)
        p += tp
        pos += v

    for e in p:
        print(e, end=" ")
    print("")
