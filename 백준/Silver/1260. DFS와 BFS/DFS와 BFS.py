import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
adj = {i: [] for i in range(1, N+1)}
for (a, b) in edges:
    adj[a].append(b)
    adj[b].append(a)

for i in adj:
    adj[i].sort()

stack = [V]
dfs_visited = [0]*(N+1)
dfs_result = []

while stack:
    cur = stack.pop()
    if not dfs_visited[cur]:
        dfs_result.append(cur)
        dfs_visited[cur] = 1
    
    for a in reversed(adj[cur]):
        if not dfs_visited[a]:
            stack.append(a)

q = deque([V])
bfs_visited = [0]*(N+1)
bfs_result = []

while q:
    cur = q.popleft()
    bfs_visited[cur] = 1
    bfs_result.append(cur)

    for a in adj[cur]:
        if not bfs_visited[a]:
            bfs_visited[a] = 1
            q.append(a)

print(*dfs_result, sep=" ")
print(*bfs_result, sep=" ")
