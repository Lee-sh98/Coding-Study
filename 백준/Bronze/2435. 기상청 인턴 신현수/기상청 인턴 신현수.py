import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
acc = [0]*(N+1)
result = -100_000
for i in range(N):
    acc[i+1] = acc[i]+arr[i]

for i in range(N-K+1):
    result = max(result, acc[i+K]-acc[i])

print(result)
