import sys
input = sys.stdin.readline

MAX = 2*123_456+1
prime = [1]*MAX
chk = [0]*MAX

for i in range(2, MAX):
    if chk[i]:
        continue
    chk[i] = 1
    for j in range(i<<1, MAX, i):
        chk[j] = 1
        prime[j] = 0

while n:=int(input()):
    print(sum(prime[n+1:2*n+1]))
    
