(N,a,b),*c=[[*map(int,i.split())]for i in open(0)]
print(("HAPPY","ANGRY")[c[a-1][b-1]<max(c[a-1]+[d[b-1]for d in c])])
