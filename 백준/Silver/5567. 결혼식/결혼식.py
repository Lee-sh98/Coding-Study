import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
visited = [0]*(n+1)
edges = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

stack = [(1, 0)]
while stack:
    cur, depth = stack.pop()
    visited[cur] = 1
    if depth>=2:
        continue
    for node in edges[cur]:
        if not visited[node]:
            stack.append((node, depth+1))

print(sum(visited)-1)
