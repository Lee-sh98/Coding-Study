import sys
input = lambda: map(int, sys.stdin.readline().split())

N, = input()
edges = [[] for _ in range(N+1)]
seq = []

for _ in range(N-1):
    u, v = input()
    seq.append((u, v))
    edges[u].append(v)
    edges[v].append(u)

cut_node = lambda k: len(edges[k])>1
q, = input()
for _ in range(q):
    t, k = input()
    print(("no", "yes")[cut_node(k) if 2-t else True])
