t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    s = list(input())
    max_char_position = 0
    while k > 0:
        max_char = s[max_char_position]
        for c in s:
            c_val = ord(c) - 97
            if c_val > k:
                break
            if c_val > ord(max_char) - 97:
                max_char = c

        temp_mc_pos = s.index(max_char)
        replacement_char = chr(ord(max_char) - min(k, ord(max_char) - 97))
        for pos, c in enumerate(s[max_char_position:]):
            pos += max_char_position
            if c <= max_char and c > replacement_char:
                s[pos] = replacement_char
        k -= ord(max_char) - 97
        max_char_position = temp_mc_pos + 1
    
    print("".join(s))