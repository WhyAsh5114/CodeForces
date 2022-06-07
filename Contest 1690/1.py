for _ in range(int(input())):
    n = int(input())
    base = n // 3
    h1, h2, h3 = base, base, base
    rem = n % 3
    if rem > 0:
        h1 += 1
        rem -= 1
    if rem > 0:
        h1 += 1
        rem -= 1
    if rem > 0:
        h2 += 1
        rem -= 1
    
    while h1 <= h2 or h2 <= h3:
        if h2 <= h3:
            h3 -= 1
            h2 += 1
        if h1 <= h2:
            h1 += 1
            h2 -= 1
    
    print(h2, h1, h3)