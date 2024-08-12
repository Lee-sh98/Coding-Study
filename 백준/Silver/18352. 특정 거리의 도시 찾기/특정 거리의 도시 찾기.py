import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, M, distance_target, X = map(int, input().split())
edges = defaultdict(list)
distance_scale = 1

for _ in range(M):
    A, B = map(int, input().split())
    edges[A].append(B)

# BFS
visited = [0]*(N+1)
result = [0]*(N+1)
q = deque([(X, 0)])
while q:
    cur, distance = q.popleft()
    visited[cur] = 1
    if distance == distance_target:
        result[cur] = 1
        continue
    for node in edges[cur]:
        if visited[node]:
            continue
        q.append((node, distance + distance_scale))
        visited[node] = 1

if any(result):
    for i, _ in filter(lambda x: x[1], enumerate(result)):
        print(i)
else:
    print(-1)
