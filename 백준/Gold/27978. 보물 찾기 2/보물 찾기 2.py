from heapq import*
f,*s=[*open(0)]
H,W=map(int,f.split())
d=[W*[9**9]for _ in range(H)]
Q=[]
for x in range(H*W):Q+=[(0,x//W,x%W)]*('K'==s[x//W][x%W])
while Q:
 c,x,y=heappop(Q)
 if'*'==s[x][y]:exit(print(c))
 if d[x][y]<c:continue
 for u,v in zip([-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]):
  p,q,r=x+u,y+v,c+(v<1)
  if 0<=p<H and 0<=q<W and'#'!=s[p][q]and r<d[p][q]:d[p][q]=r;heappush(Q,(r,p,q))
print(-1)