for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]

    cost = sum(a)
    if cost < m:
        print(0)
    else:
        print(cost - m)