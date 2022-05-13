t = int(input())

answers = []
for i in range(t):
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]

    a.sort()
    d = {}
    for n in a:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    
    invalid = []
    for key in d:
        if d[key] < k:
            invalid.append(key)
    for num in invalid:
        d.pop(num)
    
    valid = list(d.keys())
    valid.append(0)
    pairs = []
    l = valid[0]
    r = valid[0]
    for j in range(1, len(valid)):
        if abs(valid[j] - valid[j-1]) > 1:
            pairs.append([l, r])
            l = valid[j]
        else:
            r = valid[j]
    
    max_lr = 0
    max_pair = -1
    for pair in pairs:
        diff = pair[1] - pair[0]
        if diff > max_lr:
            max_lr = diff
            max_pair = pair
    if max_pair != -1:
        answers.append([max_pair[0], max_pair[1]])
    elif len(valid) > 1:
        answers.append([valid[0], valid[0]])
    else:
        answers.append(-1)

for ans in answers:
    if ans == -1:
        print(ans)
    else:
        print(ans[0], ans[1])