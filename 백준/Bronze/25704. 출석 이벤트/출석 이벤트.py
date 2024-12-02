N=int(input())
P=int(input())
Q=min(max((0,500,P//10,2000,P*25//100)[:N//5+1]),P)
print(P-Q)