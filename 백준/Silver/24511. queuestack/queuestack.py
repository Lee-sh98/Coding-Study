import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = map(int, input().split())
B = map(int, input().split())
M = int(input())
C = list(map(int, input().split()))

dq = C[::-1]+[b for a, b in zip(A, B) if not a]

print(*dq[::-1][:M])
