import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = float('inf')
arr = [int(input()) for _ in range(N)]
arr.sort()
i, j = 0, 0

while i<=j<N:
    diff = arr[j] - arr[i]

    if diff>= M:
        result = min(result, diff)
        i += 1
    else:
        j += 1

print(result)
