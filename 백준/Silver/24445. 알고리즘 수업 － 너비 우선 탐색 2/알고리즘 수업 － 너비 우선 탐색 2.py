import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
edges = [[] for _ in range(N+1)]
result = [0]*(N+1)
sequence = 0

for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

for i in range(N+1):
    edges[i].sort(reverse=True)

q = deque([R])
while q:
    cur = q.popleft()
    result[cur] = (sequence:=sequence+1)

    for node in edges[cur]:
        if not result[node]:
            result[node] = -1
            q.append(node)

for i in range(1, N+1):
    print(result[i])
