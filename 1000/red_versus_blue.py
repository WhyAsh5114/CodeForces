from math import ceil


for _ in range(int(input())):
    n, r, b = map(int, input().split())
    s = ['R'] * n
    p = n / (b + 1)
    pos = p - 1
    while b > 0:
        place_pos = ceil(pos)
        s[place_pos] = "B"
        pos += p
        b -= 1
    print("".join(s))
