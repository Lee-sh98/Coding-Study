import sys
input = sys.stdin.readline

n, k = map(int, input().split())
children = [[] for _ in range(n)]

for _ in range(n-1):
    p, c = map(int, input().split())
    children[p].append(c)

apples = list(map(int, input().split()))

stack = [(0, 0)]
result = 0
while stack:
    cur, depth = stack.pop()
    if depth > k:
        continue
    if apples[cur]:
        result += 1
    for child in children[cur]:
        stack.append((child, depth+1))

print(result)
