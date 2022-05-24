for _ in range(int(input())):
    n = int(input())
    s = list(input())
    mid = (n-1) // 2
    to_right = 0
    right_mid = mid + 1
    while right_mid < len(s) and s[right_mid] == s[mid]:
        to_right += 1
        right_mid += 1
    left_mid = mid - 1
    to_left = 0
    while s[left_mid] == s[mid] and left_mid >= 0:
        to_left += 1
        left_mid -= 1
    print(to_left + to_right + 1)
