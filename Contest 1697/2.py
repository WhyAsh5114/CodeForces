from sys import stdin, stdout

print = lambda x: stdout.write(str(x) + "\n")


n, q = map(int, input().split())
p = [int(x) for x in input().split()]
p.sort(reverse=True)
 
for i in range(1, n):
    p[i] += p[i-1]

for i in range(q):
    x, y = map(int, input().split())
    if x != y:
        stdout.write(str(p[x-1] - p[x-y-1]) + "\n")
    else:
        stdout.write(str(p[x-1]) + "\n")
