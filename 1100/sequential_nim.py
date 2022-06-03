for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]

    if max(a) == 1:
        if n % 2 == 0:
            print("Second")
        else:
            print("First")
        continue
    
    cnt = 0
    for e in a:
        if e == 1:
            cnt += 1
        else:
            break
    
    if cnt % 2 == 0:
        print("First")
    else:
        print("Second")
