from heapq import *
R,F=range,9**9
f,*s=[*open(0)]
H,W=map(int,f.split())
e=[(i,j)for j in R(-1,2)for i in R(-1,2)if not(i==j==0)]
d=[W*[F]for _ in R(H)]
for x in R(H*W):
 i,j=x//W,x%W
 if'K'==s[i][j]:Q=[(0,i,j)];d[i][j]=0
while Q:
 c,x,y=heappop(Q)
 if'*'==s[x][y]:exit(print(c))
 if d[x][y]<c:continue
 for u,v in e:
  p,q,r=x+u,y+v,c+(v<1)
  if 0<=p<H and 0<=q<W and'#'!=s[p][q]and r<d[p][q]:d[p][q]=r;heappush(Q,(r,p,q))
print(-1)