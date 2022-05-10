t = int(input())

a = []
for i in range(t):
    n, m = [int(x) for x in input().split()]
    case = []
    for j in range(n):
        case.append(input())
    a.append(case)

for case in a:
    diffs = []
    for i in range(len(case)):
        for j in range(len(case)):
            if i == j:
                continue
            aa = list(case[i])
            ab = list(case[j])
            a = []
            b = []
            for c in aa:
                a.append(ord(c))
            for c in ab:
                b.append(ord(c))
            
            diff = 0
            for c1, c2 in zip(a, b):
                diff += min(abs(c2 - c1), abs(c1 - c2))
            diffs.append(diff)
    
    print(min(diffs))
