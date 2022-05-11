t = int(input())

answers = []
for i in range(t):
    n, q = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort(reverse=True)
    for j in range(len(a)-1):
        a[j+1] += a[j]

    total_sugar = sum(a)
    for j in range(q):
        x = int(input())
        low = 0
        high = len(a) - 1

        answer = -1
        while low <= high:
            mid = (low + high) // 2
            if a[mid] >= x:
                answer = mid + 1
                high = mid - 1
            else:
                low = mid + 1
        answers.append(answer)

print("\nOUTPUT:")
for answer in answers:
    print(answer)
