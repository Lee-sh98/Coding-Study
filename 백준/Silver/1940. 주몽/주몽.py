import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
i, j = 0, N-1

while i<j:
    s = arr[i] + arr[j]
    if s == M:
        result += 1
        i += 1
    elif s > M:
        j -= 1
    else:
        i += 1

print(result)
