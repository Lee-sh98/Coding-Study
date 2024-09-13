import sys
from heapq import *
input = sys.stdin.readline

def dijkstra(x, y):
    distances = [[float('inf')]*n for _ in range(n)]
    distances[x][y] = 0

    q = []
    heappush(q, (0, x, y))

    while q:
        broken, cx, cy = heappop(q)

        if distances[cx][cy] < broken:
            continue

        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy

            if not(0<=nx<n and 0<=ny<n):
                continue
            cost = broken + int(not graph[nx][ny])

            if cost<distances[nx][ny]:
                distances[nx][ny] = cost
                heappush(q, (cost, nx, ny))
    return distances

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

result = dijkstra(0, 0)
print(result[n-1][n-1])
