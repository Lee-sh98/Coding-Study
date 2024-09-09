import sys
input = sys.stdin.readline

def dfs(root):
    parents = [-1]*(N+1)
    parents[root] = root
    stack = [(root, 0)]

    while stack:
        cur, depth = stack.pop()

        for node, _ in edges[cur]:
            if parents[node] == -1:
                parents[node] = cur
                level[node] = depth+1
                stack.append((node, depth+1))
    return parents

def NCA(a, b):
    result = 0

    while level[a] != level[b]:
        if level[a] > level[b]:
            pa = parents[a]
            result += distances[a, pa]
            a = pa
        else:
            pb = parents[b]
            result += distances[b, pb]
            b = pb

    while a!=b:
        pa = parents[a]
        pb = parents[b]

        result += distances[a, pa] + distances[b, pb]
        a, b = pa, pb
        
    return result

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
distances = {}
level = [0]*(N+1)

for _ in range(N-1):
    u, v, w = map(int, input().split())

    distances[u, v] = w
    distances[v, u] = w

    edges[u].append([v, w])
    edges[v].append([u, w])

root = 1
parents = dfs(root)

for _ in range(M):
    a, b = map(int, input().split())
    result = NCA(a, b)
    print(result)
