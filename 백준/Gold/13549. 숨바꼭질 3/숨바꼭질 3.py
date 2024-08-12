import sys
from heapq import *

def valid(target):
    return 0<=target<MAX_NODE

def walk_back(cur, cost):
    return cur-1, cost+1

def walk_front(cur, cost):
    return cur+1, cost+1

def teleport(cur, cost):
    return cur*2, cost

N, K = map(int, sys.stdin.readline().split())
MAX_NODE = 100001
distance = [float('inf')]*MAX_NODE
distance[N] = 0
actions = [walk_back, walk_front, teleport]

q = []
heappush(q, (0, N))
while q:
    cur_distance, cur = heappop(q)

    if distance[cur] < cur_distance:
        continue

    for action in actions:
        next_node, next_distance = action(cur, cur_distance)
        if not valid(next_node):
            continue

        if next_distance < distance[next_node]:
            distance[next_node] = next_distance
            heappush(q, (next_distance, next_node))

print(distance[K])
