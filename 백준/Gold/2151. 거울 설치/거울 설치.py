import sys
from collections import deque
input = sys.stdin.readline

DOOR = "#"
WALL = "*"
MIRROR = "!"
EMPTY = "."

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
visited = [[[-1]*4 for _ in range(N)] for _ in range(N)]
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
doors = []


for i in range(N):
    for j in range(N):
        if arr[i][j] == DOOR:
            doors.append((i, j))

(sx, sy), (ex, ey) = doors
q = deque()
for i in range(4):
    visited[sx][sy][i] = 0
    q.append((sx, sy, i))
result = int(1e9)
while q:
    cx, cy, cd = q.popleft()
    if cx==ex and cy==ey:
        result = min(result, visited[cx][cy][cd])
        continue
    
    dx, dy = directions[cd]
    nx, ny = cx + dx, cy + dy

    if not(0<=nx<N and 0<=ny<N):
        continue
    if arr[nx][ny] == WALL:
        continue

    if visited[nx][ny][cd] == -1 or visited[nx][ny][cd] > visited[cx][cy][cd]:
        visited[nx][ny][cd] = visited[cx][cy][cd]
        q.append((nx, ny, cd))

    if arr[nx][ny] == MIRROR:
        for dd in [-1, 1]:
            nd = (cd+dd)%4
            if visited[nx][ny][nd] == -1 or visited[nx][ny][nd] > visited[cx][cy][cd]:
                visited[nx][ny][nd] = visited[cx][cy][cd] + 1
                q.append((nx, ny, nd))

print(result)
