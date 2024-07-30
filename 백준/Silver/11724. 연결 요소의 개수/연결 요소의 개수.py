# 11724 connected component

import sys
from collections import deque
input = sys.stdin.readline


def traverse(node: int):
    q = deque([node])

    while q:
        cur = q.popleft()

        visited[cur] = 1

        for x in edges[cur]:
            if not visited[x]:
                visited[x] = 1
                q.append(x)

N, M = map(int, input().split())
edges = {x:set() for x in range(1,N+1)}

for _ in range(M):
    u, v  = map(int, input().split())
    edges[u].add(v)
    edges[v].add(u)

component = 0
visited = [0]*(N+1)

for i in range(1, N+1):
    if not visited[i]:
        component += 1
        traverse(i)

print(component)
