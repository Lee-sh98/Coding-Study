import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
INF = int(1e10)

def solve(x, acc, M):
    global visited
    if x == B:
        return M
    result = INF
    for node, cost in edges[x]:
        if not visited[node]:
            visited[node] = 1
            if acc+cost <= C:
                result = min(result, solve(node, acc+cost, max(M, cost)))
            visited[node] = 0
    return result

N, M, A, B, C = map(int, input().split())
edges = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    u, v, l = map(int, input().split())
    edges[u].append((v, l))
    edges[v].append((u, l))

result = solve(1, 0, 0)
print((result, -1)[result==INF])
