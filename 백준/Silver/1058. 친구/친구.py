import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map("Y".__eq__, input().rstrip())) for _ in range(N)]
friends = [g[:] for g in graph]

for i in range(N):
    for j in filter(i.__ne__, range(N)):
        for k in filter(lambda x: x not in [i, j], range(N)):
            if graph[i][k] and graph[k][j]:
                friends[i][j] = True

print(max(sum(f) for f in friends))
