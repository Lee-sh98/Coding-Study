def f(s,d):
    if d==N:
        if eval(s.replace(' ',''))==0:result.append(s)
    else:
        for i in" +-":f(s+i+str(d+1),d+1)
for _ in" "*int(input()):N=int(input());result=[];f("1",1);print(*sorted(result),sep="\n");print()