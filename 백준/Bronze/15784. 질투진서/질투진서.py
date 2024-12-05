N,a,b=map(int,input().split())
arr=[[*map(int,input().split())] for _ in range(N)]
print(("HAPPY","ANGRY")[any(map(arr[a-1][b-1].__lt__,arr[a-1]+[*map(list,zip(*arr))][b-1]))])