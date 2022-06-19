answers = []

for _ in range(int(input())):
    n, s = map(int, input().split())
    a = [int(x) for x in input().split()]
    total = sum(a)
    diff = total - s

    if s > total:
        answers.append(-1)
        continue
    elif s == total:
        answers.append(0)
        continue

    ta = a.copy()
    lp = [0]
    for i in range(n):
        if ta[i] == 1:
            lp.append(i+1)
    
    ta.reverse()
    rp = [0]
    for i in range(n):
        if ta[i] == 1:
            rp.append(i+1)

    ans = n
    for i in range(diff + 1):
        ans = min(lp[diff-i] + rp[i], ans)
    answers.append(ans)

for ans in answers:
    print(ans)