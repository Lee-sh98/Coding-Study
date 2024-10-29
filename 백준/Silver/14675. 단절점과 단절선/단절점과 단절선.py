import sys
input = lambda: map(int, sys.stdin.readline().split())

N, = input()
edges = [0]*(N+1)

for _ in range(N-1):
    for i in input():
        edges[i]+=1

q, = input()
for _ in range(q):
    t, k = input()
    print(("yes", "no")[t==1 and edges[k]==1])
