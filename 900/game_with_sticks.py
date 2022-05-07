m, n = [int(x) for x in input().split()]

intersections = m * n
move_count = -1
while intersections > 0:
    intersections -= (m - 1) + (n - 1) + 1
    m -= 1
    n -= 1
    move_count += 1

if move_count % 2 == 0:
    print("Akshat")
else:
    print("Malvika")