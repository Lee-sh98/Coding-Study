import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

result = -100*K
start, end = 0, K-1
total = sum(arr[start:end])

while end<N:
    total += arr[end]
    result = max(result, total)
    total -= arr[start]

    start += 1
    end += 1

print(result)
