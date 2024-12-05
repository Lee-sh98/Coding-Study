(N,a,b),*c=[[*map(int,i.split())]for i in open(0)]
print(("HAPPY","ANGRY")[any(map(c[a-1][b-1].__lt__,c[a-1]+[*map(list,zip(*c))][b-1]))])