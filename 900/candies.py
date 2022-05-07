t = int(input())
na = []
for i in range(t):
    na.append(int(input()))

for n in na:
    for k in range(2, 30):
        if n % (2**k - 1) == 0:
            print(int(n / (2**k - 1)))
            break