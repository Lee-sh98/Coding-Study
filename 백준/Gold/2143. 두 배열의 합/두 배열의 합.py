import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

acc = [0]*(n+1)
for i in range(n):
    acc[i+1] = acc[i] + A[i]

bcc = [0]*(m+1)
for j in range(m):
    bcc[j+1] = bcc[j] + B[j]

c = Counter()
for i in range(n):
    for j in range(i+1, n+1):
        c[acc[j]-acc[i]] += 1

result = 0
for i in range(m):
    for j in range(i+1, m+1):
        t = T - (bcc[j] - bcc[i])
        result += c[t]

print(result)
