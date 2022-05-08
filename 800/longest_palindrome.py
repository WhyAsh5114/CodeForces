n, m = [int(x) for x in input().split()]

all_strings = set()
for i in range(n):
    all_strings.add(input())

start = []
end = []
individual_string = ""
for s in all_strings:
    if s[::-1] in all_strings and s not in start and s not in end and s != s[::-1]:
        start.append(s)
        end.append(s[::-1])
    elif s == s[::-1]:
        individual_string = s

start = "".join(start)
end = "".join(reversed(end))
answer = start + individual_string + end
print(len(answer))
print(answer)
