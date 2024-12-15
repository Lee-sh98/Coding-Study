T=int(input())
month=[31,30]*3+[30,31]*3
month[1]=29
month[6]=31

for _ in range(T):
    a=input().replace(" ","")
    b=[i for i in range(1,13) if a[i%10]=="0" and (i<10 or (9<i and a[1]=="0"))]
    c=[*filter(lambda i: a[i%10]=="0" and (i<10 or (9<i and a[i//10]=="0")),range(1,32))]
    d=sum(sum(map(month[i-1].__ge__, c)) for i in b)
    print(d)
