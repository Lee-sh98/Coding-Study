import sys
from collections import deque
input = sys.stdin.readline

def lca(a, b):
    if d[a] > d[b]:
        a, b = b, a
    while d[a] != d[b]:
        b = parent[b]

    while a!=b:
        a = parent[a]
        b = parent[b]
    return a

N = int(input())
parent = [0]*(N+1)
d = [-1]*(N+1)
d[1] = 0
edges = [[] for _ in range(N+1)]

for i in range(N-1):
    A, B = map(int, input().split())
    edges[A].append(B)
    edges[B].append(A)

q = deque([1])
while q:
    cur = q.popleft()
    for node in edges[cur]:
        if d[node] == -1:
            d[node] = d[cur] + 1
            parent[node] = cur
            q.append(node)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))
