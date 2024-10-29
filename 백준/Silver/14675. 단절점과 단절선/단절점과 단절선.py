import sys
input = lambda: map(int, sys.stdin.readline().split())

N, = input()
edges = [0]*(N+1)

for _ in range(N-1):
    u, v = input()
    edges[u]+=1
    edges[v]+=1

q, = input()
for _ in range(q):
    t, k = input()
    print(("no", "yes")[edges[k]>1 or t==2])
