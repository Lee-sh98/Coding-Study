(P,),*Q=[[*map(int,i.split())]for i in open(0)]
for K,b,n in Q:
    t=0
    while n>0:
        n,r=divmod(n,b)
        t+=r**2
    print(K,t)