s = [int(x) for x in list(input())]

team1 = 0
team2 = 0
for p in s:
    if p == 0:
        team1 += 1
        team2 = 0
    else:
        team2 += 1
        team1 = 0
    
    if team1 == 7 or team2 == 7:
        print("YES")
        break
else:
    print("NO")