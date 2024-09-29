import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e9)

def dijkstra():
    if arr[0][0] == -1 or arr[m-1][n-1] == -1:
        return -1
    distances = [[INF]*n for _ in range(m)]
    distances[0][0] = arr[0][0]

    q = [(distances[0][0], 0, 0)]
    while q:
        dist, x, y = heappop(q)

        if distances[x][y] < dist:
            continue

        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if not(0<=nx<m and 0<=ny<n):
                continue
            if arr[nx][ny] == -1:
                continue
            cost = dist + arr[nx][ny]
            if cost<distances[nx][ny]:
                distances[nx][ny] = cost
                heappush(q, (cost, nx, ny))
    return distances[m-1][n-1]

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

result = dijkstra()
print((result, -1)[result==INF])
