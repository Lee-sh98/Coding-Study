import sys
sys.setrecursionlimit(10**6)

def f(c,s):
    if w[c][s]:
        return w[c][s]
    w[c][s] = p[c]*s
    for d in r[c]:
        w[c][s]+=max(f(d,0),f(d,1)*(1-s))
    return w[c][s]

(N,),p,*s=[[*map(int,i.split())]for i in open(0)]
p = [0]+p
q,r,w = zip(*[[[],[],[0]*2]for _ in range(N+1)])
for A,B in s:
    q[A].append(B);q[B].append(A)
t = [1]
while t:
    c = t.pop()
    for d in q[c]:
        if not r[d]:
            r[c].append(d)
            t.append(d)
print(max(f(1, 0), f(1, 1)))
