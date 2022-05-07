n = int(input())

all_s = []
for i in range(n):
    all_s.append(input())

for s in all_s:
    if len(s) > 10:
        print(s[0] + str(len(s)-2) + s[-1])
    else:
        print(s)