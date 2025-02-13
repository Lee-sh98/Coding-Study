N=int(input())
X,S=map(int, input().split())
r=0
for _ in range(N):
    c,p=map(int, input().split())
    if c<=X:r=max(r,p)
print("YNEOS"[r<=S::2])