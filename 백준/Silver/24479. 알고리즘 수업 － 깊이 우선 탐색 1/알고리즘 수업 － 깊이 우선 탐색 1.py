import sys
from collections import defaultdict
input = sys.stdin.readline


N, M, R = map(int, input().split())
edges = defaultdict(list)

visited = [0]*(N+1)
count = 1

for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

for i in edges:
    edges[i].sort(reverse=True)

stack = [R]
while stack:
    cur = stack.pop()

    if visited[cur]:
        continue

    visited[cur] = count
    count += 1

    for v in edges[cur]:
        stack.append(v)

for v in visited[1:]:
    print(v)
