T=int(input())
month=[0]+[31,30]*3+[30,31]*3
month[2]=29
month[7]=31

for _ in range(T):
    a=[*input().split()]
    b={str(i) for i in range(10) if a[i]=="0"}

    c={int(x+y) for y in b for x in b if int(x+y)<13}
    d={int(x+y) for y in b for x in b if int(x+y)<32}

    e={*map(int,(b|c)-{"0",0})}
    f={*map(int,(b|d)-{"0",0})}
    g=sum(sum(map(month[x].__ge__,f)) for x in e)

    print(g)
