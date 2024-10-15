import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

j = 0
odds, evens = 0, 0
result = 0

for i in range(N):
    while j<N and odds<=K:
        if arr[j]%2:
            odds += 1
        else:
            evens += 1
        j += 1
    
    result = max(result, evens)
    if arr[i]%2:
        odds -= 1
    else:
        evens -= 1

print(result)
