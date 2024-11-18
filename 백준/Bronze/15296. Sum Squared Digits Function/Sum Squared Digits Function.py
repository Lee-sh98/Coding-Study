for K,b,n in [[*map(int,i.split())]for i in open(0)][1:]:
    t=0
    while n:n,r=divmod(n,b);t+=r**2
    print(K,t)