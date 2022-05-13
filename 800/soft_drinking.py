n, k, l, c, d, p, nl, np = map(int, input().split())

each_drink = (l*k // nl)
lime_slices = c*d
salt_needed = p // np

answer = min(each_drink, lime_slices, salt_needed) // n
print(answer)