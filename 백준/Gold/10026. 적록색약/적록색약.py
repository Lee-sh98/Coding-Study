import sys
input = sys.stdin.readline

def dfs(graph, i, j):
    target = graph[i][j]
    q = [(i, j)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        cx, cy = q.pop()
        graph[cx][cy] = 0

        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]

            if 0<=nx<N and 0<=ny<N and graph[nx][ny] == target:
                q.append((nx, ny))

def inspect(graph):
    result = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                dfs(graph, i, j)
                result += 1
    return result

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
modified_graph = []
for i in range(N):
    tmp = [0]*N
    for j in range(N):
        if graph[i][j] == "B":
            tmp[j] = "B"
        else:
            tmp[j] = "T"
    modified_graph.append(tmp)

graph_count = inspect(graph)
modified_graph_count = inspect(modified_graph)

print(graph_count, modified_graph_count)
