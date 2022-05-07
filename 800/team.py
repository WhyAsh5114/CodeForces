n = int(input())

problems = []
for i in range(n):
    problems.append([int(x) for x in input().split()])

solutions = 0
for problem in problems:
    if sum(problem) >= 2:
        solutions += 1

print(solutions)