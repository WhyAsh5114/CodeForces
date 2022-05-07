s = input().split("WUB")
for w in s:
    if w == "":
        s.remove(w)

s = " ".join(s)
print(s)