answers = []
for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    
    for i in range(0, n-1):
        if abs(a[i] - a[i+1]) + abs(b[i] - b[i+1]) > abs(a[i] - b[i+1]) + abs(b[i] - a[i+1]):
            a[i+1], b[i+1] = b[i+1], a[i+1]

    ans = 0
    for i in range(n-1):
        ans += abs(a[i] - a[i+1]) + abs(b[i] - b[i+1])
    answers.append(ans)


for ans in answers:
    print(ans)