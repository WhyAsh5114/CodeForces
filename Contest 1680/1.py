t = int(input())

answers = []
for i in range(t):
    l1, r1, l2, r2 = map(int, input().split())
    if (max(l1, l2) <= min(r1, r2)):
        answers.append(max(l1, l2))
    else:
        answers.append(l1+l2)

for ans in answers:
    print(ans)