import sys
from collections import deque
input = lambda: map(int, sys.stdin.readline().split())

L, N, K = input()
lights = list(input())
street = [-1]*(L+1)

q = deque((0, light) for light in lights)
for l in lights:
    street[l] = 0

while q:
    brightness, cur = q.popleft()
    
    for d in [-1, 1]:
        node = cur+d
        
        if 0<=node<=L and street[node]==-1:
            street[node] = brightness+1
            q.append((brightness+1, node))

print("\n".join(map(str, sorted(street)[:K])))
