import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

distances = [[INF]*M for _ in range(N)]
distances[x1-1][y1-1] = 0
q = [(0, x1-1, y1-1)]

while q:
    dist, x, y = heappop(q)
    if distances[x][y] < dist:
        continue
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if not(0<=nx<N and 0<=ny<M):
            continue
        cost = dist+int(arr[nx][ny]=='1')
        if cost < distances[nx][ny]:
            distances[nx][ny] = cost
            heappush(q, (cost, nx, ny))

print(distances[x2-1][y2-1]+1)
