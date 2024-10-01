import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur, count):
    if cur==P:
        broken.append(count)
        return
    visited[cur] = True
    for node in edges[cur]:
        if not visited[node]:
            dfs(node, count+1)
    

N, S, P = map(int, input().split())
edges = [[] for _ in range(N+1)]
visited = [False]*(N+1)
broken = []

for _ in range(N-1):
    A, B = map(int, input().split())
    edges[A].append(B)
    edges[B].append(A)

for i in range(1, S+1):
    dfs(i, 0)
broken.sort()

print(N-broken[0]-broken[1]-1)
