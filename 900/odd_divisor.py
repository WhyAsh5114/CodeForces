t = int(input())

a = []
for i in range(t):
    a.append(int(input()))

for n in a:
    while n % 2 == 0:
        n /= 2
    if n == 1:
        print("NO")
    else:
        print("YES")