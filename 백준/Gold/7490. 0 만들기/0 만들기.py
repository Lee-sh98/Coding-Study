def f(s,d):
    if d==N:
        if eval(s.replace(' ',''))==0:print(s)
    else:
        for i in" +-":f(s+i+str(d+1),d+1)
T,*M=map(int,open(0))
for N in M:f("1",1);print()