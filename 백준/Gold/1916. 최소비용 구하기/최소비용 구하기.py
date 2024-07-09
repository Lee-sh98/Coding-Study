import sys
from heapq import *
input = sys.stdin.readline

N = int(input())
M = int(input())
distances = {i: 1e9 for i in range(N+1)}
graph = {i: [] for i in range(N+1)}
for _ in range(M):
    a, b, distance = map(int, input().split())
    graph[a].append((b, distance))
S, E = map(int, input().split())

distances[S] = 0
q = []
heappush(q, [distances[S], S])

while q:
    cur_distance, cur_destination = heappop(q)

    if distances[cur_destination] < cur_distance:
        continue
    for new_destination, new_distance in graph[cur_destination]:
        distance = cur_distance + new_distance
        if distance < distances[new_destination]:
            distances[new_destination] = distance
            heappush(q, [distance, new_destination])
print(distances[E])
