for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())

    ans = k
    sum = 0
    for i in range(k):
        if s[i] == 'W':
            sum += 1
    ans = min(sum, ans)
    
    for i in range(k, n):
        if s[i] == 'W' and s[i-k] == 'B':
            sum += 1
        elif s[i] == 'B' and s[i-k] == 'W':
            sum -= 1
        ans = min(sum, ans)

    print(ans)
