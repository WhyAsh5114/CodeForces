t = int(input())

answers = []
for i in range(t):
    n = int(input())
    s = input()
    s = s.split("W")
    while '' in s:
        s.remove('')
    possible = True
    for sub in s:
        if not (len(sub) >= 2 and 'B' in sub and 'R' in sub):
            answers.append("NO")
            possible = False
            break
    if possible:
        answers.append("YES")


for ans in answers:
    print(ans)