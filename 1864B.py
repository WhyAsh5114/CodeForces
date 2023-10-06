t = int(input())

answers = []
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    s = list(input())
    s.sort()
    answers.append("".join(s))

for ans in answers:
    print(ans)