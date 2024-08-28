import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

F = [0]*N
count = Counter(A)

for i in range(N):
    F[i] = count[A[i]]


NGF = [-1]*N
stack = []
for i in range(N):
    while stack and F[stack[-1]]<F[i]:
        NGF[stack.pop()] = A[i]
    stack.append(i)

print(" ".join(map(str, NGF)))
