import sys
from collections import deque
input = sys.stdin.readline

def find_all_unions():
    visited = [[False]*N for _ in range(N)]
    unions = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union = []
                q=  deque([(i, j)])
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    union.append((x, y))
                    for dx, dy in directions:
                        nx, ny = x+dx, y+dy
                        if not (0<=nx<N and 0<=ny<N):
                            continue
                        if L<=abs(arr[x][y]-arr[nx][ny])<=R and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                if len(union) >= 2:
                    unions.append(union)
    return unions

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
days = 0

while True:
    unions = find_all_unions()
    if len(unions) == 0:
        break
    for union in unions:
        S = sum(map(lambda x: arr[x[0]][x[1]], union))
        length = len(union)
        population = S//length
        for ux, uy in union:
            arr[ux][uy] = population

    days += 1

print(days)
