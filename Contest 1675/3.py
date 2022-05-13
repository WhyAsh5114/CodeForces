t = int(input())

for i in range(t):
    s = input()
    last_one = 0
    first_zero = len(s)-1
    if len(s) == 1:
        print(1)
        continue
    if '1' in s:
        last_one = s.rindex('1')
    if '0' in s:
        first_zero = s.index('0')
    s = list(s)
    s = s[last_one:first_zero+1]
    print(len(s))
