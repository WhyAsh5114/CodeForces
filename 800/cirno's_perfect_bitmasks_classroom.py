for _ in range(int(input())):
    x = int(input())
    y = 1
    if x == 1:
        print(3)
        continue

    while (x & y) == 0:
        y = y << 1

    if (x ^ y) == 0:
        y = list(bin(y)[2:])
        y[-1] = '1'
        y = "".join(y)
        y = int(y, 2)

    print(y)