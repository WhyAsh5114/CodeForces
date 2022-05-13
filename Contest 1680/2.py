t = int(input())

answers = []
for i in range(t):
    n, m = map(int, input().split())
    grid = []
    for j in range(n):
        s = list(input())
        row = []
        for c in s:
            if c == 'E':
                row.append(0)
            else:
                row.append(1)
        grid.append(row)
    
    first_row = grid[0]
    while 1 not in grid[0]:
        for y in range(1, n):
            grid[y-1] = grid[y]
        last_row = []
        for x in range(m):
            last_row.append(0)
        grid[-1] = last_row
    
    closest = grid[0].index(1)
    ans = True
    for y in range(1, n):
        for x in range(closest):
            if grid[y][x] != 0:
                ans = False
                break
        if not ans:
            break
    answers.append(ans)

for ans in answers:
    if ans:
        print("YES")
    else:
        print("NO")