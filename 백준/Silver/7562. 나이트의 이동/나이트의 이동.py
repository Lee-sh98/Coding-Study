import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
dx = [2, 2, 1, -1, -2, -2, -1, 1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

def bfs():
    N = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    visited = [[0]*N for _ in range(N)]
    q = deque([(sx, sy)])
    
    while q:
        cx, cy = q.popleft()

        if cx == ex and cy == ey:
            return visited[cx][cy]

        for d in range(8):
            nx = cx + dx[d]
            ny = cy + dy[d]

            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                visited[nx][ny] = visited[cx][cy] + 1
                q.append((nx, ny))
    

for _ in range(T):
    print(bfs())
