(N,a,b),*arr=[[*map(int,i.split())]for i in open(0)]
print(("HAPPY","ANGRY")[any(map(arr[a-1][b-1].__lt__,arr[a-1]+[*map(list,zip(*arr))][b-1]))])