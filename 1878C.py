t = int(input())

answers = []
for _ in range(t):
    n, k, x = [int(x) for x in input().split()]
    if x >= (k*(k+1))/2 and x <= (n*(n+1) - (n-k)*(n-k+1)) / 2:
        answers.append("YES")
    else:
        answers.append("NO")

for ans in answers:
    print(ans)
