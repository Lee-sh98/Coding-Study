import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque([(x, y)])
    count = 0

    while q:
        cx, cy = q.popleft()
        board[cx][cy] = 1
        count += 1
        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<M and 0<=ny<N and board[nx][ny] == 0:
                board[nx][ny] = 1
                q.append((nx, ny))
    
    return count

N, M, K = map(int, input().split())
board = [[0]*N for _ in range(M)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1

components = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            components.append(bfs(i, j))

print(len(components))
print(*sorted(components))
