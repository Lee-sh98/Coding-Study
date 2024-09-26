import sys
from collections import deque
input = sys.stdin.readline

def make_tree():
    children = [[] for _ in range(N+1)]
    stack = [1]
    while stack:
        cur = stack.pop()

        for node in edges[cur]:
            if not children[node]:
                children[cur].append(node)
                stack.append(node)
    return children

N, W = map(int, input().split())
water = [0]*(N+1)
water[1] = W
edges = [[] for _ in range(N+1)]


for _ in range(N-1):
    U, V = map(int, input().split())
    edges[U].append(V)
    edges[V].append(U)

children = make_tree()
q = deque([1])
while q:
    cur = q.popleft()
    if not children[cur]:
        continue
    each_water = water[cur]/len(children[cur])
    water[cur] = 0
    for node in children[cur]:
        water[node] += each_water
        q.append(node)

count = 0
for i in range(1, N+1):
    if water[i]:
        count += 1

print(W/count)
