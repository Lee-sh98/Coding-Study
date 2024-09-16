import sys
from collections import deque
input = sys.stdin.readline

N, M, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)]
DX = [1, -1, 0, 0, 0, 0]
DY = [0, 0, 1, -1, 0, 0]
DZ = [0, 0, 0, 0, 1, -1]

q = deque()

for x in range(H):
    for y in range(M):
        for z in range(N):
            if arr[x][y][z]==1:
                q.append((x, y, z))

while q:
    x, y, z = q.popleft()

    for dx, dy, dz in zip(DX, DY, DZ):
        nx, ny, nz = x+dx, y+dy, z+dz

        if not(0<=nx<H and 0<=ny<M and 0<=nz<N):
            continue

        if arr[nx][ny][nz] == 0:
            arr[nx][ny][nz] = arr[x][y][z] + 1
            q.append((nx, ny, nz))

matured = all(all(all(line) for line in floor) for floor in arr)

if matured:
    print(max(max(max(line) for line in floor) for floor in arr)-1)
else:
    print(-1)
