import sys
f = lambda: map(int, sys.stdin.readline().split())

N, = f()
e = [0]*(N+1)

for _ in range(N-1):
    for i in f():
        e[i]+=1

q, = f()
for _ in range(q):
    t, k = f()
    print(("yes", "no")[t==1 and e[k]==1])
