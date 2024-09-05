import sys
input = sys.stdin.readline

def dfs(graph, s):
    distances = [-1]*(len(graph)+1)
    stack = [(s, 0)]

    while stack:
        cur, dist = stack.pop()
        distances[cur] = dist

        for node, next_dist in graph[cur]:
            if distances[node] == -1:
                stack.append((node, dist+next_dist))
    idx = 0
    for i in range(len(graph)+1):
        if distances[idx] < distances[i]:
            idx = i
    return idx, distances[idx]

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

tmp, _ = dfs(graph, 1)
_, dist = dfs(graph, tmp)

print(dist)
