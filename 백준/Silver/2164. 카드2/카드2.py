import sys
from math import *
def func(N):
    M = 2**floor(log2(N))
    last = 2*(N-M)
    return (N, last)[last!=0]

N = int(sys.stdin.readline())

print(func(N))
