import sys
input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(start):
    distance[start] = 0
    for i in range(1, N+1):
        for S, E, T in edges:
            cost = distance[S] + T
            if cost == INF:
                continue
            if distance[E] > cost:
                distance[E] = cost
                if i == N:
                    return True
    return False

T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split())
    distance = [INF]*(N+1)
    edges = []

    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
        
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    if bellman_ford(1):
        print("YES")
    else:
        print("NO")
