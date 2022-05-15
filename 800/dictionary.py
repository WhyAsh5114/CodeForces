t = int(input())

for i in range(t):
    s = input()
    fp = (ord(s[0]) - 97) * 25
    fs = (ord(s[1]) - 96)
    if (s[1] > s[0]):
        fs -= 1
    
    print(fp + fs)