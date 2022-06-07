answers = []

for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    max_diff = 0
    valid = True
    for i in range(n):
        if a[i] - b[i] < 0:
            answers.append("NO")
            valid = False
            break
        if a[i] - b[i] > max_diff:
            max_diff = a[i] - b[i]
        
    if not valid:
        continue

    for i in range(n):
        diff = a[i] - b[i]
        if diff != max_diff:
            if b[i] != 0:
                answers.append("NO")
                break
    else:
        answers.append("YES")


for ans in answers:
    print(ans)
    