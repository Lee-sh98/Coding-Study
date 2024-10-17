import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e8)
A = ord('A')
a = ord('a')

def input_line():
    result = []
    for c in map(ord,input().rstrip()):
        if A <= c <= A+25:
            result.append(c - A)
        else:
            result.append(c - a + 26)
    return result

def dijkstra(sx, sy, compare):
    distance = [[INF]*M for _ in range(N)]
    distance[sx][sy] = 0

    q = [(0, sx, sy)]
    while q:
        dist, x, y = heappop(q)
        if distance[x][y] < dist:
            continue
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if not (0<=nx<N and 0<=ny<M):
                continue

            dh = graph[x][y]-graph[nx][ny]
            if abs(dh) > T:
                continue

            cost = dist + (1 if compare(dh) else dh**2)
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heappush(q, (cost, nx, ny))
    return distance

def solve(sx, sy):
    ascend = dijkstra(0, 0, int(0).__le__)
    descend = dijkstra(0, 0, int(0).__ge__)
    
    MAX = 0
    for i in range(N):
        for j in range(M):
            if ascend[i][j]+descend[i][j]<=D and MAX < graph[i][j]:
                MAX = graph[i][j]
    return MAX

N, M, T, D = map(int, input().split())
graph = [input_line() for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

result = solve(0, 0)
print(result)
