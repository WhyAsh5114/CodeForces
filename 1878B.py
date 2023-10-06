t = int(input())

answers = []
for _ in range(t):
    n = int(input())
    a = [1]
    s = 1
    for i in range(n-1):
        s += 2
        a.append(s)
    answers.append(a)

for ans in answers:
    for n in ans:
        print(n, end=" ")
    print()
