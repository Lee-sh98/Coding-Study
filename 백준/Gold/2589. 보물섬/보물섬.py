import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    visited = [[0]*M for _ in range(N)]
    visited[x][y] = 1
    q = deque([(x, y, 0)])
    result = 0
    while q:
        cx, cy, dist = q.popleft()
        result = max(result, dist)

        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy

            if not(0<=nx<N and 0<=ny<M):
                continue
            if not visited[nx][ny] and arr[nx][ny] == "L":
                visited[nx][ny] = 1
                q.append((nx, ny, dist+1))
    
    return result
        
    
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
result = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == "L":
            result = max(result, bfs(i, j))

print(result)
