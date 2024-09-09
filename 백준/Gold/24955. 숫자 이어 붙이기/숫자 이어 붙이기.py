import sys
input = sys.stdin.readline


N, Q = map(int, input().split())
arr = [""]+list(input().split())
edges = [[] for _ in range(N+1)]
root = 1
parents = [-1]*(N+1)
level = [0]*(N+1)
MOD = 1_000_000_007

for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

parents[root] = root
stack = [(root, 0)]
while stack:
    cur, depth = stack.pop()
    level[cur] = depth
    for c in edges[cur]:
        if parents[c] == -1:
            parents[c] = cur
            stack.append((c, depth+1))
            
for _ in range(Q):
    x, y = map(int, input().split())
    left, right = [], []

    while level[x] != level[y]:
        if level[x] > level[y]:
            left.append(arr[x])
            x = parents[x]
        else:
            right.append(arr[y])
            y = parents[y]

    while x!=y:
        left.append(arr[x])
        right.append(arr[y])
        x = parents[x]
        y = parents[y]

    left.append(arr[x])

    while right:
        left.append(right.pop())

    print(int("".join(left))%MOD)
    
