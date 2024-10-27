import sys
input = sys.stdin.readline

def solve():
    S = input().rstrip()
    l, r = 0, len(S)-1
    
    while l<=r:
        if S[l] == S[r]:
            l += 1
            r -= 1
        else:
            left = S[l:r]
            right = S[l+1:r+1]
            if left == left[::-1]:
                return 1
            elif right == right[::-1]:
                return 1
            else:
                return 2
    return 0

T = int(input())
for _ in range(T):
    print(solve())
