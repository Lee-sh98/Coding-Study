#2798 black jack

m=int(input().split()[1])
inp=set(map(int,input().split()))

res=[]
for i in inp:
    for j in inp-{i}:
        for k in inp-{i,j}:
            if i+j+k<=m:
                res.append(i+j+k)
print(max(res))