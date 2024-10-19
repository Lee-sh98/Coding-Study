import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
king = input().rstrip()
value = defaultdict(int)
graph = defaultdict(list)

for _ in range(N):
    child, left, right = input().split()

    graph[left].append(child)
    graph[right].append(child)

stack = [(king, 1)]
while stack:
    cur, val = stack.pop()
    value[cur] += val
    for child in graph[cur]:
        stack.append((child, val/2))

name = ""
for _ in range(M):
    cur = input().rstrip()
    if value.get(name, 0) < value.get(cur, 0):
        name = cur

print(name)
