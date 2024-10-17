import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e10)

def dijkstra(sx, sy):
    distances = [[INF]*N for _ in range(N)]
    distances[sx][sy] = 0

    q = [(0, sx, sy)]
    while q:
        dist, x, y = heappop(q)

        if distances[x][y] < dist:
            continue
        for dx, dy in directions:
            nx, ny = x+dx, y+dy

            if not (0<=nx<N and 0<=ny<N):
                continue
            cost = max(dist, abs(arr[nx][ny]-arr[x][y]))

            if cost < distances[nx][ny]:
                distances[nx][ny] = cost
                heappush(q, (cost, nx, ny))

    return distances[N-1][N-1]
        

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

result = dijkstra(0, 0)
print(result)
