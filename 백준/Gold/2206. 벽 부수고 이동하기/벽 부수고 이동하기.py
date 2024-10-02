import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    q = deque([(0, 0, 0)])
    
    while q:
        x, y, broken = q.popleft()
        
        if x==N-1 and y==M-1:
            return visited[N-1][M-1][broken]
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if not(0<=nx<N and 0<=ny<M):
                continue
            if arr[nx][ny] == 1 and broken == 0:
                visited[nx][ny][1] = visited[x][y][0]+1
                q.append((nx, ny, 1))
            elif arr[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                visited[nx][ny][broken] = visited[x][y][broken]+1
                q.append((nx, ny, broken))
    return -1
    

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

result = bfs()
print(result)
