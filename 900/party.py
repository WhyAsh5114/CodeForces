import sys
sys.setrecursionlimit(2001)

n = int(input())

roots = []
adj = {}
for i in range(1, n+1):
    p = int(input())
    if p == -1:
        roots.append(i)
    else:
        if p not in adj:
            adj[p] = [i]
        else:
            adj[p].append(i)

def find_depth(node):
    global adj
    if node not in adj:
        return 1
    else:
        max_depth = 0
        for child in adj[node]:
            depth = 1 + find_depth(child)
            if depth > max_depth:
                max_depth = depth
        return max_depth

max_root_depth = 0
for root in roots:
    root_depth = find_depth(root)
    if root_depth > max_root_depth:
        max_root_depth = root_depth

print(max_root_depth)