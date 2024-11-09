import sys
input = sys.stdin.readline

def dfs(start, cur):
    visited[start][cur] = 1
    visited[cur][start] = 1
    for taller in edges[cur]:
        if not visited[start][taller]:
            dfs(start, taller)

N, M = map(int, input().split())
visited = [[0]*N for _ in range(N)]
edges = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)

for i in range(N):
    dfs(i, i)

print(sum(map(lambda i: sum(visited[i])==N, range(N))))
