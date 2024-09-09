import sys
from math import log2
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())

    while int(log2(A)) != int(log2(B)):
        if log2(A) > log2(B):
            A >>= 1
        else:
            B >>= 1

    while A != B:
        A >>= 1
        B >>= 1
    print(A*10)
