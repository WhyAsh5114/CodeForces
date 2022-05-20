n, q = map(int, input().split())
a = [int(x) for x in input().split()]

ans = sum(a)
lsv, lsq = 0, -1
lfv, lfq = a, [-1]*n

for i in range(q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        query[1] -= 1
        if lfq[query[1]] < lsq:
            ans += query[2] - lsv
            lfq[query[1]] = i
            lfv[query[1]] = query[2]
        else:
            ans += query[2] - lfv[query[1]]
            lfq[query[1]] = i
            lfv[query[1]] = query[2]
    else:
        lsv = query[1]
        lsq = i
        ans = query[1] * n
    print(ans)
