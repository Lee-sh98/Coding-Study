import sys

K, N, M = map(int, sys.stdin.readline().split())
print(max(K*N-M, 0))
