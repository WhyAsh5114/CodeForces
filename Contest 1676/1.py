t = int(input())

n = []
for i in range(t):
    n.append(list(input()))

for num in n:
    ns = []
    for digit in num:
        ns.append(int(digit))
    a = sum(ns[0:3])
    b = sum(ns[3:6])
    if a == b:
        print("YES")
    else:
        print("NO")
