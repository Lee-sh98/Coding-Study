import sys
from itertools import *
input = sys.stdin.readline

x = [input().rstrip() for _ in range(5)]

for y in zip_longest(*x, fillvalue=""):
    print(*y,sep="",end="")
