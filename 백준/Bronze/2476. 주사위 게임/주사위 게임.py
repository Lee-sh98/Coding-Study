r=0
for s in [*open(0)][1:]:
    a,b,c=map(int,s.split())
    if a==b==c:t=10000+a*1000
    elif a==b or b==c or c==a:t=1000+(c,a)[a==b]*100
    else:t=max(a,b,c)*100
    r=max(r,t)
print(r)
