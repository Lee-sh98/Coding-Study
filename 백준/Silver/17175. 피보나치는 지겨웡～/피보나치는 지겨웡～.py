a=b=1
for i in range(int(input())):a,b=b,(a+b+1)%1000000007
print(a)