answers = []

for _ in range(int(input())):
    s, x = input().split()
    x = int(x)

    s = s.split(":")
    h = int(s[0])
    m = int(s[1])

    ih, im = h, m
    ma = x % 60
    ha = x // 60

    started = False
    palindromes = set()
    while not (h == ih and m == im) or not started:
        sh = list(str(h))
        if h < 10:
            sh = ['0'] + sh
        sh.reverse()
        sm = list(str(m))
        if m < 10:
            sm = ['0'] + sm
        if sh == sm:
            sh.reverse()
            palindromes.add(f"{sh} {sm}")
        h += ha
        m += ma
        if h > 23:
            h %= 24
        if m > 59:
            h += 1
            m = m % 60
            if h == 24:
                h = 0
        started = True

    answers.append(len(palindromes))

for ans in answers:
    print(ans)