import sys

N, K = map(int, sys.stdin.readline().split())
count = 0

while bin(N).count('1') > K:
    idx = bin(N)[::-1].index('1')
    count += 2**idx
    N += 2**idx

print(count)
