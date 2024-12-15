month=[31,29]+[31,30,31,30,31]*2
for a in[*open(0)][1:]:
    a=a.replace(" ","")
    b=[i for i in range(1,13) if a[i%10]=="0" and (i<10 or (9<i and a[1]=="0"))]
    c=[*filter(lambda i: a[i%10]=="0" and (i<10 or (9<i and a[i//10]=="0")),range(1,32))]
    d=sum(sum(map(month[i-1].__ge__, c)) for i in b)
    print(d)