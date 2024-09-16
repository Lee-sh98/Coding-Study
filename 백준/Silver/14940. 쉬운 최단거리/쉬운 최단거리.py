import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
sx, sy = 0, 0
for i in range(n):
    for j, v in enumerate(map(int, input().split())):
        if v:
            arr[i][j] = v-2
            if v==2:
                sx, sy = i, j
        else:
            arr[i][j] = 0

q = deque([(sx, sy)])
DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]

while q:
    cx, cy = q.popleft()
    
    for dx, dy in zip(DX, DY):
        nx, ny = cx + dx, cy + dy

        if 0<=nx<n and 0<=ny<m and arr[nx][ny]==-1:
            arr[nx][ny] = arr[cx][cy] + 1
            q.append((nx, ny))

for line in arr:
    print(" ".join(map(str, line)))
