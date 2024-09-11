import sys
from heapq import  *
input = sys.stdin.readline

def dijkstra(graph, x, y):
    distances = [[float('inf')]*N for _ in range(N)]
    distances[x][y] = graph[x][y]

    q = []
    heappush(q, (graph[x][y], x, y))

    while q:
        dist, cx, cy = heappop(q)
        

        if distances[cx][cy]<dist:
            continue
        
        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy
            
            if not (0<=nx<N and 0<=ny<N):
                continue
            
            cost = dist+graph[nx][ny]
            if cost < distances[nx][ny]:
                distances[nx][ny] = cost
                heappush(q, (cost, nx, ny))

    return distances
    
i = 1
directions = [(1, 0), (-1, 0), (0,  1), (0, -1)]
while True:
    N = int(input())

    if not N:
        break

    arr = [list(map(int, input().split())) for _ in range(N)]
    route = dijkstra(arr, 0, 0)
    print(f"Problem {i}: {route[N-1][N-1]}")
    i+=1
