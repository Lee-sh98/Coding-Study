N,L,H,*A=map(int,open(0).read().split())
print(sum([*sorted(A)][L:N-H])/(N-L-H))