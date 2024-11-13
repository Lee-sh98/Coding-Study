n=int(input())
if n<3:
    print(0)
else:
    p,q,r=range(3)
    for i in range(3,n+1):
        p+=q
        q+=r
        r+=1
    print(p)
print(3)
