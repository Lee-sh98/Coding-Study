import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

j = 0
odds = 0
length = 0
result = 0

for i in range(N):
    while j<N and odds<=K:
        odds += arr[j]%2
        length += 1-arr[j]%2
        j += 1
    
    result = max(result, length)
    odds -= arr[i]%2
    length -= 1-arr[i]%2

print(result)
