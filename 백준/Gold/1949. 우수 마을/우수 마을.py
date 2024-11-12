import sys
sys.setrecursionlimit(9**6)
def f(c):
    for d in q[c]:
        if v[d]:v[d]=0;f(d);w[c][0]+=w[d][1];w[c][1]+=max(w[d])
(N,),p,*s=[[*map(int,i.split())]for i in open(0)]
q,r,w=zip(*[[[],[],[p[i],0]]for i in range(N)])
v=[0]+[1]*N
for A,B in s:q[A-1].append(B-1);q[B-1].append(A-1)
f(0)
print(max(w[0]))
