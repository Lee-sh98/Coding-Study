import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())
light = [0]*(N+1)

for _ in range(B):
    light[int(input())] = 1

for i in range(1, N+1):
    light[i] += light[i-1]

result = K
for i in range(1, N-K+1):
    result = min(result, light[i+K]-light[i])

print(result)
