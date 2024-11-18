for K,b,n in [map(int,i.split())for i in open(0)][1:]:
    t=0
    while n:t+=(n%b)**2;n//=b
    print(K,t)