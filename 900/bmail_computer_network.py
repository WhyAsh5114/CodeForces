n = int(input())
p = [int(x) for x in input().split()]

path = []
current = n
while current != 1:
    path.append(current)
    current = p[current-2]
path.append(1)
path.reverse()

for e in path:
    print(e, end=" ")
print()