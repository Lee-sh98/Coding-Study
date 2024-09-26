import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [0]*1_000_001
end = 0
result = 0

for _ in range(N):
    g, x = map(int, input().split())
    arr[x] = g
    end = max(end, x)

step = 2*K+1
total = sum(arr[:step])
result = total

for i in range(step, end+1):
    total += arr[i] - arr[i-step]
    result = max(result, total)

print(result)
