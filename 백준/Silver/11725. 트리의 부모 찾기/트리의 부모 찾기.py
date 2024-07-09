import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
edges = {i: set() for i in range(1, N+1)}
for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].add(b)
    edges[b].add(a)

parent = list(range(N+1))
q = deque([(1, -1)])
prev = 1

while q:
    cur, par = q.popleft()
    for i in edges[cur]:
        if parent[i] == i:
            parent[i] = cur
            q.append([i,cur])

print(*parent[2:], sep="\n")
