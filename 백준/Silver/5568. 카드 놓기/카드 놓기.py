import sys
input = sys.stdin.readline

def solve(x, c):
    if c==k:
        result.add(x)
    else:
        for i in range(n):
            if not used[i]:
                used[i] = 1
                solve(x+arr[i], c+1)
                used[i] = 0

n, k = [int(input()) for _ in range(2)]
arr = [input().rstrip() for _ in range(n)]
used = [0]*n
result = set()
solve("", 0)
print(len(result))
