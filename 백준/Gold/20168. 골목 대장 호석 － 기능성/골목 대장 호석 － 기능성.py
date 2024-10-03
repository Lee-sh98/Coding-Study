import sys
input = sys.stdin.readline
INF = int(1e10)

def solve(cur, total_cost, max_cost):
    global result
    if total_cost > C:
        return
    if cur == B:
        result = min(result, max_cost)
        return
    for node, cost in edges[cur]:
        if not visited[node]:
            visited[node] = True
            solve(node, total_cost+cost, max(max_cost, cost))
            visited[node] = False
    return

N, M, A, B, C = map(int, input().split())
edges = [[] for _ in range(N+1)]
visited = [False]*(N+1)
visited[A] = True
result = INF

for _ in range(M):
    u, v, l = map(int, input().split())
    edges[u].append((v, l))
    edges[v].append((u, l))

solve(A, 0, 0)
if result == INF:
    result = -1
print(result)
