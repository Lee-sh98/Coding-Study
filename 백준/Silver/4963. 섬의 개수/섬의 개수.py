# 4963 number of islands

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, visited, island):
    q = deque([(x, y)])
    
    while q:
        cx, cy = q.popleft()
        visited[cx][cy] = 1

        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy
            if not(0<=nx<h and 0<=ny<w):
                continue
            if island[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
    return visited


def solution(w, h):
    island = [[0]*w for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    lands = set()
    count = 0
    
    for i in range(h):
        for j, v in enumerate(map(int, input().split())):
            island[i][j] = v
            if v:
                lands.add((i, j))
    
    for x, y in lands:
        if not visited[x][y]:
            count += 1
            visited = bfs(x, y, visited, island)
    print(count)

directions = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]

while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    solution(w, h)
