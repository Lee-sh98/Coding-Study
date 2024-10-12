import sys
input = sys.stdin.readline
INF = float('inf')

def bellman_ford(start):
    distance[start] = 0
    for i in range(1, V+1):
        for A, B, C in edges:
            cost = distance[A]+C
            if cost == INF:
                continue
            if distance[B] > cost:
                distance[B] = cost
                if i==V:
                    return True

    return False      

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
distance = [INF]*(V+1)

if bellman_ford(1):
    print(-1)
else:
    for d in distance[2:]:
        print((d, -1)[d==INF])
