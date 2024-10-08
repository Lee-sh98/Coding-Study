import sys
input = sys.stdin.readline

def recursion(s, l, r, d):
    if l>=r:
        return 1, d
    elif s[l] != s[r]:
        return 0, d
    else:
        return recursion(s, l+1, r-1, d+1)

def is_palindrome(s):
    return recursion(s, 0, len(s)-1, 1)

N = int(input())
for _ in range(N):
    print(*is_palindrome(input().rstrip()))
