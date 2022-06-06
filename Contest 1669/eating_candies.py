answers = []

for _ in range(int(input())):
    n = int(input())
    w = [int(x) for x in input().split()]

    i = 0
    j = n - 1

    a = 0
    b = 0
    
    ans = 0
    while i <= j:
        a += w[i]
        i += 1
        while a > b and i <= j:
            b += w[j]
            j -= 1
        if a == b:
            ans = (i) + (n - 1 - j)
    
    answers.append(ans)


for ans in answers:
    print(ans)
