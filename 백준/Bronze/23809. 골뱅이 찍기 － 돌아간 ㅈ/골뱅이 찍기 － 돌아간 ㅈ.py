N=int(input())
A="@"*N
f=lambda s:[A+s+A]*N
print(*(a:=f(" "*3*N)),*(b:=f(" "*2*N)),*f(A),*b,*a,sep="\n")