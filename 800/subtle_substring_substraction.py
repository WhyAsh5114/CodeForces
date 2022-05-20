for _ in range(int(input())):
    s = list(input())
    a, b = 0, 0
    if len(s) >= 2:
        if len(s) % 2 == 0:
            for e in s:
                a += ord(e) - 96
        else:
            left = s[0:len(s)]
            right = s[1:len(s)]
            left_sum = 0
            right_sum = 0
            for e1, e2 in zip(left, right):
                left_sum += ord(e1) - 96
                right_sum += ord(e2) - 96
            if left_sum > right_sum:
                a += left_sum
                s = s[-1]
            else:
                a += right_sum
                s = s[0]
            b += ord(s) - 96
    else:
        b = ord(s[0]) - 96
    
    if a > b:
        print("Alice", a-b)
    else:
        print("Bob", b-a)
