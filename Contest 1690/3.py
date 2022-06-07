answers = []

for _ in range(int(input())):
    n = int(input())
    s = [int(x) for x in input().split()]
    f = [int(x) for x in input().split()]

    d = []
    current_task = None
    for i in range(n-1):
        if f[i] < s[i+1] and current_task is None:
            d.append(f[i] - s[i])
        else:
            if current_task is None:
                current_task = i
                d.append(f[current_task] - s[i])
            else:
                d.append(f[i] - f[current_task])
                current_task = i
            if f[i] < s[i+1]:
                current_task = None
    
    if current_task is None:
        d.append(f[-1] - s[-1])
    else:
        d.append(f[-1] - f[current_task])
    
    answers.append(d)


for ans in answers:
    for e in ans:
        print(e, end=" ")
    print("")
