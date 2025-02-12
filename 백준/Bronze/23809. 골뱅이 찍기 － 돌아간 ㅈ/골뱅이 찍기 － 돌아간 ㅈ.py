N=int(input())
f=lambda s:["@"*N+s*N+"@"*N]*N
print(*(a:=f(" "*3)),*(b:=f(" "*2)),*f("@"),*b,*a,sep="\n")