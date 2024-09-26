import sys
input = sys.stdin.readline

N, W = map(int, input().split())
edges = [0]*(N+1)
result = 0

for _ in range(N-1):
    U, V = map(int, input().split())
    edges[U] += 1
    edges[V] += 1

for i in range(2, N+1):
    if edges[i] == 1:
        result += 1

print(W/result)
