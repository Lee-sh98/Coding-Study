# 17298 NGE

import sys
input = sys.stdin.readline


N = int(input())
A = list(enumerate(map(int, input().split())))
stack = []
stack.append(A[0])
result = [-1]*N

for i, a in A[1:]:
    while stack and stack[-1][1] < a:
        j, _ = stack.pop()
        result[j] = a
    stack.append((i, a))

print(" ".join(map(str, result)))
