n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

advanced = 0
for e in a:
    if e >= a[k-1] and e > 0:
        advanced += 1
    else:
        break

print(advanced)
