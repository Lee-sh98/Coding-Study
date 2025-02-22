while (n:=int(input()))+1:
    a=[]
    for _ in range(n):
        *i,m,b=*input().split(),1
        for j in i:b*=int(j)
        a+=[(b,m)]
    print(max(a)[1],'took clay from',min(a)[1]+'.')
