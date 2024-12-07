n=int(input())
a=[*map(int,input().split())]
b=0
for i in a:
    for j in a:
        b+=abs(i-j)
print(b)