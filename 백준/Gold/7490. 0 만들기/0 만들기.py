def f(s,d):
    if d==N:
        if eval(s.replace(' ',''))==0:r.append(s)
    else:
        for i in" +-":f(s+i+str(d+1),d+1)
for _ in" "*int(input()):N=int(input());r=[];f("1",1);print(*r,"",sep="\n")