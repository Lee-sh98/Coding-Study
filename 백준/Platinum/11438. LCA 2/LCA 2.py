import sys
from math import log2
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
logN = 21

def dfs(node):
    visited[node] = True

    for c in edges[node]:
        if visited[c]:
            continue
        parents[c][0] = node
        levels[c] = levels[node] + 1
        dfs(c)

def LCA(A, B):
    if levels[A] > levels[B]:
        A, B = B, A

    for i in range(logN-1, -1, -1):
        if levels[B]-levels[A] >= (1<<i):
            B = parents[B][i]

    if A==B:
        return A
    
    for i in range(logN-1, -1, -1):
        if parents[A][i] != parents[B][i]:
            A = parents[A][i]
            B = parents[B][i]

    return parents[A][0]

N = int(input())
visited = [False]*(N+1)
levels = [0]*(N+1)
parents = [[0]*logN for _ in range(N+1)]
edges = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

dfs(1)

for j in range(1, logN):
    for i in range(1, N+1):
        parents[i][j] = parents[parents[i][j-1]][j-1]

M = int(input())

for _ in range(M):
    A, B = map(int, input().split())

    print(LCA(A, B))
