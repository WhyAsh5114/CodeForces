n = int(input())
a = [int(x) for x in input().split()]

max_subsegment = 0
local_max = 10**9 + 1
current_max_subsegment = 0
for e in a:
    if e < local_max:
        if current_max_subsegment > max_subsegment:
            max_subsegment = current_max_subsegment
        local_max = e
        current_max_subsegment = 1
    else:
        local_max = e
        current_max_subsegment += 1

if current_max_subsegment > max_subsegment:
    max_subsegment = current_max_subsegment
print(max_subsegment)