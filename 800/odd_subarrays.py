for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]

    i = 0
    cnt = 0
    while i < n-1:
        if a[i] > a[i + 1]:
            cnt += 1
            i += 1
        i += 1

    print(cnt)
