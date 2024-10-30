import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    screen[x][y] = 0

    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<M and screen[nx][ny]:
            dfs(nx, ny)

N, M = map(int, input().split())
screen = [[0]*M for _ in range(N)]
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        screen[i][j] = sum(line[3*j:3*j+3])

T = int(input())
for i in range(N):
    for j in range(M):
        screen[i][j] = (screen[i][j]/3>=T)*255

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
count = 0
for i in range(N):
    for j in range(M):
        if screen[i][j]:
            count+=1
            dfs(i, j)

print(count)
