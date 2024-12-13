import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e9)

H, W = map(int, input().split())
tx, ty = 0,0
sea = [input().rstrip() for _ in range(H)]
directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
distances = [[INF]*W for _ in range(H)]
q = []

for i in range(H):
    for j in range(W):
        if sea[i][j] == 'K':
            heappush(q, (0, i, j))
            distances[i][j] = 0
        elif sea[i][j] == '*':
            tx, ty = i, j

while q:
    dist, x, y = heappop(q)
    if x==tx and y==ty:
        break
    if distances[x][y] < dist:
        continue
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        ndist = dist+(dy!=1)
        if not(0<=nx<H and 0<=ny<W) or sea[nx][ny] == '#':
            continue
        if ndist<distances[nx][ny]:
            distances[nx][ny] = ndist
            heappush(q, (ndist, nx, ny))

if distances[tx][ty]==INF:distances[tx][ty]=-1
print(distances[tx][ty])
