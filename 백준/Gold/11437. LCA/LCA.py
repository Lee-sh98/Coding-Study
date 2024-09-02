import sys
from collections import deque
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def memoize(func):
    memo = {}
    def helper(a, b):
        if (a, b) not in memo:
            memo[a, b] = func(a, b)
        return memo[a, b]
    return helper

def lca(a, b):
    if d[a] > d[b]:
        return lca(parent[a], b)
    elif d[a] < d[b]:
        return lca(a, parent[b])
    while a!=b:
        a = parent[a]
        b = parent[b]
    return a
lca = memoize(lca)

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
