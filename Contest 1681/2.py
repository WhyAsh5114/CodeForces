for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    m = int(input())
    b = [int(x) for x in input().split()]

    print(a[sum(b) % n])
