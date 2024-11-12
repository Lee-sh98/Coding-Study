import sys
sys.setrecursionlimit(9**6)
def f(c):
    for d in q[c]:
        if p[d]:p[d]=0;f(d);w[c][0]+=w[d][1];w[c][1]+=max(w[d])
(N,),p,*s=[[*map(int,i.split())]for i in open(0)]
q,w=zip(*[[[],[t,0]]for t in p])
for A,B in s:q[A-1].append(B-1);q[B-1].append(A-1)
p[0]=0;f(0)
print(max(w[0]))