for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    moves = []
    while True:
        swaps_performed = 0
        for i in range(n-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                moves.append([i, i+1])
                swaps_performed += 1
        if swaps_performed == 0:
            break

    for pair in moves:
        b[pair[0]], b[pair[1]] = b[pair[1]], b[pair[0]]

    sorted_b = sorted(b)
    if sorted_b == b:
        print(len(moves))
        for move in moves:
            print(move[0]+1, move[1]+1)
    else:
        swaps_performed = 0
        freq = {}
        for e in a:
            if e not in freq:
                freq[e] = 1
            else:
                freq[e] += 1

        counter = 0
        for e in freq:
            if freq[e] == 1:
                counter += 1
            else:
                subset = b[counter:counter+freq[e]]
                while True:
                    swaps_performed = 0
                    for i in range(len(subset)-1):
                        if subset[i] > subset[i+1]:
                            subset[i], subset[i+1] = subset[i+1], subset[i]
                            moves.append([counter+i, counter+i+1])
                            swaps_performed += 1
                    if swaps_performed == 0:
                        break
                b[counter:counter+freq[e]] = subset
                counter += freq[e]
        if sorted_b == b:
            print(len(moves))
            for move in moves:
                print(move[0]+1, move[1]+1)
        else:
            print(-1)
